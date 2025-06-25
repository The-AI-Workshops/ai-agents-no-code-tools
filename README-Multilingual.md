# AI Agents No-Code Tools - Complete Multilingual Support

This enhanced version includes **full multilingual support** for all Kokoro TTS languages, unlocking 9 languages with 50+ voices.

## 🌍 Complete Language Support

| Language | Code | Voices | Quality | Usage Example |
|----------|------|--------|---------|---------------|
| 🇺🇸 **American English** | `a` | **20 voices** (11F, 9M) | A+ | `af_heart`, `am_adam` |
| 🇬🇧 **British English** | `b` | **8 voices** (4F, 4M) | A | `bf_emma`, `bm_george` |
| 🇯🇵 **Japanese** | `j` | **5 voices** (4F, 1M) | B+ | `jf_alpha`, `jm_kumo` |
| 🇨🇳 **Mandarin Chinese** | `z` | **8 voices** (4F, 4M) | B | `zf_xiaobei`, `zm_yunjian` |
| 🇪🇸 **Spanish** | `e` | **3 voices** (1F, 2M) | B | `ef_dora`, `em_alex` |
| 🇫🇷 **French** | `f` | **1 voice** (1F) | B- | `ff_siwis` |
| 🇮🇳 **Hindi** | `h` | **4 voices** (2F, 2M) | C+ | `hf_alpha`, `hm_omega` |
| 🇮🇹 **Italian** | `i` | **2 voices** (1F, 1M) | C | `if_sara`, `im_nicola` |
| 🇧🇷 **Portuguese** | `p` | **3 voices** (1F, 2M) | C | `pf_dora`, `pm_alex` |

## 🚀 Quick Start

### Get All Available Voices
```bash
curl "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro/voices"
```

**Response includes all 50+ voices:**
```json
{
  "voices": [
    "af_heart", "af_alloy", "af_aoede", "af_bella", "af_jessica", "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky",
    "am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam", "am_michael", "am_onyx", "am_puck", "am_santa",
    "bf_alice", "bf_emma", "bf_isabella", "bf_lily", "bm_daniel", "bm_fable", "bm_george", "bm_lewis",
    "jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro", "jm_kumo",
    "zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi", "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang",
    "ef_dora", "em_alex", "em_santa",
    "ff_siwis",
    "hf_alpha", "hf_beta", "hm_omega", "hm_psi",
    "if_sara", "im_nicola",
    "pf_dora", "pm_alex", "pm_santa"
  ]
}
```

## 🎯 Language Examples

### 🇫🇷 French
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=Bonjour, je suis un assistant IA multilingue" \
  -F "voice=ff_siwis"
```

### 🇯🇵 Japanese  
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=こんにちは、私は多言語AIアシスタントです" \
  -F "voice=jf_alpha"
```

### 🇨🇳 Chinese
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=你好，我是多语言AI助手" \
  -F "voice=zf_xiaobei"
```

### 🇪🇸 Spanish
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=Hola, soy un asistente de IA multilingüe" \
  -F "voice=ef_dora"
```

### 🇮🇳 Hindi
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=नमस्ते, मैं एक बहुभाषी AI सहायक हूं" \
  -F "voice=hf_alpha"
```

### 🇮🇹 Italian
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=Ciao, sono un assistente AI multilingue" \
  -F "voice=if_sara"
```

### 🇧🇷 Portuguese
```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=Olá, eu sou um assistente de IA multilíngue" \
  -F "voice=pf_dora"
```

## 🎬 Multilingual Video Generation

### Create videos with any language:
```bash
curl -X POST "http://localhost:3125/api/v1/media/video-tools/generate/tts-captioned-video" \
  -F "text=Your text in any supported language" \
  -F "kokoro_voice=any_voice_from_list" \
  -F "background_id=your_background_image_id"
```

## 📊 Voice Quality Guide

### 🏆 **Premium Voices (A-Grade)**
- `af_bella` 🚺🔥 - Top American English female
- `af_heart` 🚺❤️ - Flagship American English female  
- `bf_emma` 🚺 - Premium British English female

### ⭐ **High Quality (B-Grade)**
- `af_nicole` 🚺🎧 - Professional American English
- `am_fenrir` 🚹 - Strong American English male
- `jf_alpha` 🚺 - Best Japanese female
- `ff_siwis` 🚺 - French female (SIWIS dataset)

### 💬 **Standard Quality (C-Grade)**
- Most other voices in the collection
- Suitable for general usage and applications

## 🔧 Technical Features

### Enhanced Audio Processing
- **Format Compatibility**: PCM_16 format for optimal quality
- **Auto-Normalization**: Automatic audio level adjustment
- **Error Recovery**: FFmpeg fallback for problematic audio

### Robust Pipeline
- **Language Detection**: Automatic language code mapping
- **Voice Validation**: Comprehensive voice existence checking
- **Graceful Degradation**: Continues operation despite errors

### Quality Optimizations
- **Token Range**: Best performance 100-200 tokens
- **Speed Control**: Adjustable speech rate per language
- **Chunk Support**: Long text automatic segmentation

## 🐛 Known Limitations

### Language-Specific Notes
- **French**: Limited to 1 voice, may need longer text for best quality
- **Hindi/Italian/Portuguese**: Fewer voices, consider voice selection carefully
- **Japanese**: Uses specialized phonetic processing
- **Chinese**: Traditional characters may have mixed results

### Performance Tips
- **Short Utterances**: <10-20 tokens may have weaker quality
- **Long Utterances**: >400 tokens may rush, use speed adjustment
- **Non-English**: May have thinner G2P (grapheme-to-phoneme) support

## 🚀 Docker Deployment

### Build Multilingual Image
```bash
# Standard multilingual build
docker build -t ai-agents-multilingual:latest .

# CUDA-enabled for better performance  
docker build -f cuda.Dockerfile -t ai-agents-multilingual:cuda .
```

### Run Container
```bash
# CPU version
docker run -d --name ai-agents-multi -p 3125:8000 ai-agents-multilingual:latest

# GPU version (recommended for multiple languages)
docker run -d --gpus all --name ai-agents-multi-gpu -p 3125:8000 ai-agents-multilingual:cuda
```

## 📈 Performance Considerations

### Resource Usage by Language
- **English**: Lowest resource usage, fastest processing
- **Japanese/Chinese**: Moderate usage, complex character processing
- **European Languages**: Low-moderate usage, similar to English
- **Hindi**: Moderate usage, complex script processing

### Scaling Recommendations
- Use GPU acceleration for heavy multilingual workloads
- Consider language-specific containers for production
- Implement caching for frequently used voice/text combinations

## 🛠️ Development

### Adding New Languages
1. Add language config in `LANGUAGE_CONFIG`
2. Add voices in `LANGUAGE_VOICE_CONFIG`  
3. Update `supported_langs` list in TTS class
4. Test with sample text in target language

### Voice Quality Testing
```bash
# Test all voices for a language
for voice in $(curl -s "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro/voices" | jq -r '.voices[]' | grep "^jf_"); do
  echo "Testing voice: $voice"
  curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
    -F "text=これはテストです" \
    -F "voice=$voice"
done
```

## 🤝 Contributing

Contributions welcome for:
- Additional language support
- Voice quality improvements  
- Performance optimizations
- Documentation enhancements

## 📄 Credits

- **Original Project**: [AI Agents No-Code Tools](https://github.com/The-AI-Workshops/ai-agents-no-code-tools)
- **Kokoro TTS**: [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- **Multilingual Enhancement**: Claude Code Assistant
- **Voice Datasets**: Various open-source contributors (SIWIS, etc.)

---

**🌟 Now supporting 50+ voices across 9 languages with enterprise-grade reliability!**