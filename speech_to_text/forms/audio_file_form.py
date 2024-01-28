from django import forms

from speech_to_text.models import AudioFile


class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['audio_file']
