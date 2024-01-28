import whisper


class WhisperClient:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe_audio(self, file_path: None) -> str:
        try:
            print("Dentro de transcripe audio")

            result = self.model.transcribe("speech_to_text/services/audio_20230627111844.mp3")
            print(result["text"])
            return result["text"]
        except Exception as e:
            print(str(e))
            raise e
