import tkinter as tk
from tkinter import messagebox, filedialog
import speech_recognition as sr
recognizer = sr.Recognizer()


# Función para reconocer el habla desde el micrófono
def recognize_speech_from_mic(recognizer):
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


def listen_audio(recognizer, speaker, chat_history, send_query_to_ollama):
    text = recognize_speech_from_mic(recognizer)
    if text:
        response = send_query_to_ollama(text, chat_history)
        speaker.Speak(response)
        display_response(response)
    else:
        messagebox.showerror("Reconocimiento de Voz", "Lo siento, no pude entender el audio.")

# Función para mostrar respuesta
def display_response(response):
    # Verificar que la respuesta no sea None y sea de tipo string
    if response and isinstance(response, str):
        output_display.config(state=tk.NORMAL)
        output_display.delete("1.0", tk.END)  # Borrar contenido anterior
        output_display.insert(tk.END, response)  # Insertar nueva respuesta
        output_display.config(state=tk.DISABLED)
    else:
        # En caso de error, mostrar un mensaje adecuado
        messagebox.showerror("Error", "La respuesta no es válida o no se pudo procesar correctamente.")