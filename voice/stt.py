import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_telugu():
    with sr.Microphone() as source:
        print("🎤 మాట్లాడండి (Speak Telugu)...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="te-IN")
        return text
    except sr.UnknownValueError:
        return None
