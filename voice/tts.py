import os
from gtts import gTTS

def speak_telugu(text):
    tts = gTTS(text=text, lang="te")
    filename = "response.mp3"
    tts.save(filename)

    # Windows native audio playback
    os.system(f'start {filename}')
