import os

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")
# AUDIO_FILE = "speech_to_text/services/test.wav"
# use the audio file as the audio source
# print(AUDIO_FILE)


import os
import subprocess

audio_file_path = "C:\\Users\\ferna\\Documents\\DIGOTEC\\djangoProject\\speech_to_text\\services\\test.wav"
output_wav_file_path = "C:\\Users\\ferna\\Documents\\DIGOTEC\\djangoProject\\speech_to_text\\services\\converted_audio.wav"

if os.path.isfile(audio_file_path):
    try:
        # Convertir el archivo de audio a formato WAV usando FFmpeg
        subprocess.run(["ffmpeg", "-i", audio_file_path, output_wav_file_path], check=True)

        # Continuar con el reconocimiento de voz en el nuevo archivo WAV
        r = sr.Recognizer()
        with sr.AudioFile(output_wav_file_path) as source:
            audio = r.record(source)  # leer todo el archivo de audio

        # Intentar reconocer el habla utilizando Sphinx
        try:
            print("Sphinx piensa que dijiste " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx no pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error de Sphinx: {e}")

    except subprocess.CalledProcessError:
        print("Error: No se pudo convertir el archivo a formato WAV.")
    except sr.UnknownValueError:
        print("Error: No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error de solicitud: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

else:
    # El archivo no existe
    print(f"El archivo {audio_file_path} no existe.")
