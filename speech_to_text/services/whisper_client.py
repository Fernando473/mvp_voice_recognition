import os

import whisper


class WhisperClient:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe_audio(self, file_path) -> str:
        try:
            print("Dentro de transcripe audio")
            file_path = os.path.abspath(r"speech_to_text\audio_20230627102724.mp3")
            print("Archivo existe?: ", os.path.exists(file_path))
            print(file_path)
            result = self.model.transcribe(file_path)
            print(result["text"])
            return result["text"]
        except Exception as e:
            print(str(e))
            raise e
