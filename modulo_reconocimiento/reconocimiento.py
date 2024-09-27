import speech_recognition as sr

def recognize_speech(recognizer):
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio, language='es-ES')
            print("Has dicho: " + transcription)
            return transcription
        except sr.RequestError:
            print("API no disponible.")
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        return None
