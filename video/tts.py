import time
import warnings
from typing import List
from kokoro import KPipeline
import numpy as np
import soundfile as sf
from loguru import logger
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS
from video.config import device

# Suppress PyTorch warnings
warnings.filterwarnings("ignore")

LANGUAGE_CONFIG = {
    "en-us": {
        "lang_code": "a",
        "international": False,
    },
    "en": {
        "lang_code": "a",
        "international": False,
    },
    "en-gb": {
        "lang_code": "b",
        "international": False,
    },
    "es": {
        "lang_code": "e",
        "international": True,
    },
    "fr": {
        "lang_code": "f",
        "international": True,
    },
    "hi": {
        "lang_code": "h",
        "international": True,
    },
    "it": {
        "lang_code": "i",
        "international": True,
    },
    "pt": {
        "lang_code": "p",
        "international": True,
    },
    "ja": {
        "lang_code": "j",
        "international": True,
    },
    "zh": {
        "lang_code": "z",
        "international": True,
    },
}

LANGUAGE_VOICE_CONFIG = {
    "en-us": [
        "af_heart",
        "af_alloy",
        "af_aoede",
        "af_bella",
        "af_jessica",
        "af_kore",
        "af_nicole",
        "af_nova",
        "af_river",
        "af_sarah",
        "af_sky",
        "am_adam",
        "am_echo",
        "am_eric",
        "am_fenrir",
        "am_liam",
        "am_michael",
        "am_onyx",
        "am_puck",
        "am_santa",
    ],
    "en-gb": [
        "bf_alice",
        "bf_emma",
        "bf_grace",
        "bf_lily",
        "bf_poppy",
        "bm_daniel",
        "bm_george",
        "bm_james",
    ],
    "zh": [
        "zf_xiaobei",
        "zf_xiaoni",
        "zf_xiaoxue",
        "zf_xiaoyou",
        "zm_yunjian",
        "zm_yunpeng",
        "zm_yunxi",
        "zm_yunyang",
    ],
    "es": ["ef_dora", "em_alex", "em_santa"],
    "fr": ["ff_siwis"],
    "it": ["if_sara", "im_nicola"],
    "pt": ["pf_dora", "pm_alex", "pm_santa"],
    "hi": ["hf_alpha", "hf_beta", "hm_omega", "hm_psi"],
}

LANGUAGE_VOICE_MAP = {}
for lang, voices in LANGUAGE_VOICE_CONFIG.items():
    lang_config = LANGUAGE_CONFIG.get(lang, {})
    for voice in voices:
        LANGUAGE_VOICE_MAP[voice] = {
            "lang_code": lang_config.get("lang_code"),
            "international": lang_config.get("international", False),
        }


class TTS:
    def kokoro(
        self, text: str, output_path: str, voice="af_heart", speed=1
    ) -> tuple[str, List[dict], float]:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty or whitespace")
        lang_code = LANGUAGE_VOICE_MAP.get(voice, {}).get("lang_code")
        if not lang_code:
            raise ValueError(f"Voice '{voice}' not found in LANGUAGE_VOICE_MAP")
        if lang_code not in ["a", "f"]:
            raise NotImplementedError(
                f"TTS for language code '{lang_code}' is not implemented."
            )
        start = time.time()

        context_logger = logger.bind(
            voice=voice,
            speed=speed,
            text_length=len(text),
            device=device.type,
        )

        context_logger.debug("Starting TTS generation with kokoro")
        if not text or not text.strip():
            raise ValueError("Text cannot be empty or whitespace")
        pipeline = KPipeline(lang_code=lang_code, repo_id="hexgrad/Kokoro-82M", device=device)

        generator = pipeline(text, voice=voice, speed=speed)

        captions = []
        audio_data = []
        full_audio_length = 0
        for _, result in enumerate(generator):
            data = result.audio
            audio_length = len(data) / 24000
            audio_data.append(data)
            if result.tokens:
                tokens = result.tokens
                for t in tokens:
                    if t.start_ts is None or t.end_ts is None:
                        if captions:
                            captions[-1]["text"] += t.text
                            captions[-1]["end_ts"] = full_audio_length + audio_length
                        continue
                    try:
                        captions.append(
                            {
                                "text": t.text,
                                "start_ts": full_audio_length + t.start_ts,
                                "end_ts": full_audio_length + t.end_ts,
                            }
                        )
                    except Exception as e:
                        logger.error(
                            "Error processing token: {}, Error: {}",
                            t,
                            e,
                        )
                        raise ValueError(f"Error processing token: {t}, Error: {e}")
            full_audio_length += audio_length

        audio_data = np.concatenate(audio_data)
        # Ensure proper audio format for Whisper compatibility
        logger.debug(f"Audio data shape before processing: {audio_data.shape}")
        if len(audio_data.shape) > 1 and audio_data.shape[1] > 1:
            # Convert stereo to mono if needed
            audio_data = np.mean(audio_data, axis=1)
        # Ensure audio is float32 and properly normalized
        audio_data = audio_data.astype(np.float32)
        if np.max(np.abs(audio_data)) > 1.0:
            audio_data = audio_data / np.max(np.abs(audio_data))
        logger.debug(f"Audio data shape after processing: {audio_data.shape}, dtype: {audio_data.dtype}")
        # Write with explicit format for better compatibility
        sf.write(output_path, audio_data, 24000, subtype="PCM_16", format="WAV")
        context_logger.bind(
            execution_time=time.time() - start,
            audio_length=full_audio_length,
            speedup=full_audio_length / (time.time() - start),
            youtube_channel="https://www.youtube.com/@aiagentsaz"
        ).debug(
            "TTS generation completed with kokoro",
        )
        return captions, full_audio_length

    def chatterbox(
        self,
        text: str,
        output_path: str,
        sample_audio_path: str = None,
        voice: str = "en-GB-RyanNeural",
    ) -> tuple[List[dict], float]:
        start = time.time()
        context_logger = logger.bind(
            voice=voice,
            text_length=len(text),
            device=device.type,
        )
        context_logger.debug("Starting TTS generation with Chatterbox")
        if not text or not text.strip():
            raise ValueError("Text cannot be empty or whitespace")

        tts = ChatterboxTTS(model_name="xtts_v2", device=device)

        captions, audio_info = tts.tts(
            text=text,
            voice=voice,
            sample_audio_path=sample_audio_path,
            output_path=output_path,
            speed=1,
        )

        context_logger.bind(
            execution_time=time.time() - start,
            audio_length=audio_info["duration"],
            speedup=audio_info["duration"] / (time.time() - start),
            youtube_channel="https://www.youtube.com/@aiagentsaz"
        ).debug(
            "TTS generation with Chatterbox completed",
        )

    def valid_kokoro_voices(self, lang_code: str = None) -> List[str]:
        """
        Returns a list of valid voices for the given language code.
        If no language code is provided, returns all voices.
        """
        if lang_code:
            return LANGUAGE_VOICE_CONFIG.get(lang_code, [])
        else:
            return [
                voice for voices in LANGUAGE_VOICE_CONFIG.values() for voice in voices
            ]