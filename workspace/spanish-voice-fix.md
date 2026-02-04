# Spanish Voice Configuration

## Current Issue
- TTS provider: "edge" 
- Voice: "en-US-AvaNeural" (English)
- Result: Spanish with English pronunciation

## Solution Options

### Option 1: Spanish Edge Voice (Recommended)
```json
"edge": {
  "voice": "es-ES-ElviraNeural",  // Spain Spanish
  "pitch": "+0Hz",
  "rate": "+10%"
}
```

### Option 2: Mexican Spanish
```json
"edge": {
  "voice": "es-MX-DaliaNeural",  // Mexican Spanish
  "pitch": "+0Hz", 
  "rate": "+10%"
}
```

### Option 3: ElevenLabs (Premium)
Switch provider to "elevenlabs" - better quality, native pronunciation

## Command to Update
`clawdbot configure --section messages.tts`
Then update voice setting