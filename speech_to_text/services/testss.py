
import whisper
import os

model = whisper.load_model("base")

audiofile = "audio_20230627111844.mp3"
fileexists = os.path.isfile(audiofile)
print("El archivo existe? ", fileexists)
if fileexists:
    result = model.transcribe(audiofile)
    print(result["text"])
else:
    print(f"El archivo {audiofile} no existe.")