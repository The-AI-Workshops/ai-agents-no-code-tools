# AI Agents No-Code Tools - French Voice Support

This version includes enhanced French voice support using the Kokoro TTS engine with the `ff_siwis` French voice.

## 🆕 French Voice Features

- ✅ **French TTS Support**: Generate speech in French using the `ff_siwis` voice
- ✅ **Enhanced Audio Processing**: Improved audio format compatibility with Whisper
- ✅ **Robust Error Handling**: Automatic fallback and re-encoding for audio issues
- ✅ **Multi-language API**: Access all available voices including French

## 🚀 Quick Start with French Voice

### Using Docker

```bash
# Build the French-enabled image
docker build -f Dockerfile.french -t ai-agents-french:latest .

# Run the container
docker run -d --name ai-agents-french -p 3125:8000 ai-agents-french:latest
```

### Using Docker with GPU Support

```bash
# Build CUDA-enabled image
docker build -f cuda.Dockerfile -t ai-agents-french:cuda .

# Run with GPU support
docker run -d --gpus all --name ai-agents-french-gpu -p 3125:8000 ai-agents-french:cuda
```

## 📝 French Voice API Usage

### Generate French TTS

```bash
curl -X POST "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro" \
  -F "text=Bonjour, ceci est un test en français" \
  -F "voice=ff_siwis" \
  -F "speed=1.0"
```

### Get Available Voices

```bash
curl "http://localhost:3125/api/v1/media/audio-tools/tts/kokoro/voices"
```

Expected response now includes French voice:
```json
{
  "voices": [
    "af_heart", "af_alloy", "af_aoede", ...,
    "ff_siwis"
  ]
}
```

### Generate French Video with Captions

```bash
curl -X POST "http://localhost:3125/api/v1/media/video-tools/generate/tts-captioned-video" \
  -F "text=Bonjour et bienvenue dans cette démonstration" \
  -F "kokoro_voice=ff_siwis" \
  -F "background_id=your_background_image_id"
```

## 🔧 Technical Improvements

### Enhanced Audio Processing
- **Format Compatibility**: Improved PCM_16 format for better Whisper transcription
- **Mono Audio Support**: Automatic stereo-to-mono conversion when needed
- **Normalization**: Proper audio level normalization

### Error Handling
- **Graceful Degradation**: Continues processing even if transcription fails
- **FFmpeg Fallback**: Automatic audio re-encoding for compatibility issues
- **Comprehensive Logging**: Detailed debugging information

### Language Support
- **French Language Code**: `lang_code: "f"` for French processing
- **International Flag**: Proper language categorization
- **Voice Mapping**: Complete integration of `ff_siwis` voice

## 🌍 Supported Languages

| Language | Code | Voices Available | Status |
|----------|------|------------------|--------|
| English (US) | `a` | 19 voices | ✅ Full Support |
| English (GB) | `b` | 8 voices | ⚠️ Configured |
| **French** | **`f`** | **1 voice (ff_siwis)** | **✅ Full Support** |
| Spanish | `e` | 3 voices | ⚠️ Configured |
| Chinese | `z` | 8 voices | ⚠️ Configured |
| Italian | `i` | 2 voices | ⚠️ Configured |
| Portuguese | `p` | 3 voices | ⚠️ Configured |
| Hindi | `h` | 4 voices | ⚠️ Configured |
| Japanese | `j` | 0 voices | ⚠️ Configured |

## 🐛 Bug Fixes

### Fixed Issues
- **IndexError Resolution**: Resolved `tuple index out of range` errors in faster_whisper
- **Audio Format Issues**: Fixed compatibility problems between French TTS and Whisper STT
- **Voice API**: Now returns all available voices instead of English-only
- **File Path Handling**: Improved audio file path management

### Error Handling Improvements
- Automatic audio re-encoding using FFmpeg when Whisper fails
- Graceful fallback to empty captions instead of application crashes
- Detailed error logging for debugging

## 📁 Project Structure

```
├── video/
│   ├── tts.py          # Enhanced with French support
│   ├── stt.py          # Improved error handling
│   └── ...
├── Dockerfile.french   # Docker build for French support
├── README-French.md    # This file
└── ...
```

## 🔍 Troubleshooting

### Common Issues

1. **No French voice in API response**
   - Ensure you're using the updated `valid_kokoro_voices()` method
   - Check that `lang_code not in ["a", "f"]` restriction is in place

2. **Audio transcription errors**
   - The system automatically handles these with FFmpeg fallback
   - Check logs for re-encoding attempts

3. **Empty captions**
   - This is expected behavior when audio processing fails
   - Videos will still generate without captions

## 🤝 Contributing

This French voice support was added to extend the original project's capabilities. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with French and English voices
5. Submit a pull request

## 📄 License

Same as the original project.

## 🙏 Credits

- Original project: [AI Agents No-Code Tools](https://github.com/The-AI-Workshops/ai-agents-no-code-tools)
- French voice enhancement: Claude Code Assistant
- Kokoro TTS: [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)