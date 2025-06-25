from faster_whisper import WhisperModel
from loguru import logger
from video.config import device
import subprocess
import tempfile
import os


class STT:
    def __init__(self, model_size="tiny", compute_type="int8"):
        self.model = WhisperModel(model_size, compute_type=compute_type)

    def transcribe(self, audio_path, beam_size=5):
        logger.bind(
            device=device.type,
        ).debug(
            "transcribing audio with Whisper model",
        )
        
        try:
            segments, info = self.model.transcribe(
                audio_path, beam_size=beam_size, word_timestamps=True
            )
        except Exception as e:
            logger.error(f"Whisper transcription failed: {e}")
            # Try to re-encode audio using ffmpeg for compatibility
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
                tmp_path = tmp_file.name
            
            try:
                logger.debug(f"Re-encoding audio from {audio_path} to {tmp_path}")
                subprocess.run([
                    "ffmpeg", "-i", audio_path, 
                    "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", 
                    tmp_path, "-y"
                ], check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                
                segments, info = self.model.transcribe(
                    tmp_path, beam_size=beam_size, word_timestamps=True
                )
                os.unlink(tmp_path)
                logger.debug("Audio re-encoding and transcription successful")
                
            except Exception as e2:
                logger.error(f"Audio re-encoding and transcription failed: {e2}")
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
                return [], 0

        duration = info.duration
        captions = []
        for segment in segments:
            for word in segment.words:
                captions.append(
                    {
                        "text": word.word,
                        "start_ts": word.start,
                        "end_ts": word.end,
                    }
                )
        return captions, duration