import os
import tempfile

from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
from rest_framework.views import APIView

from django.shortcuts import render, redirect
from .services.whisper_client import WhisperClient


# Create your views here.

class SpeechToTextView(APIView):
    def post(self, request):
        whisper_client = WhisperClient()


# def upload_audio(request):
#     if request.method == 'POST':
#         audio_file = request.FILES.get('audio_file')
#         print(audio_file)
#         if audio_file:
#             try:
#                 # Guarda el archivo localmente
#                 audio_file_path = f"audio_temp/{audio_file.name}"
#                 with open(audio_file_path, 'wb') as audio_file_local:
#                     for chunk in audio_file.chunks():
#                         audio_file_local.write(chunk)
#
#                 # Transcribe el audio con Whisper
#                 wc = WhisperClient()
#             except Exception as e:
#                 print(f"Error en la transcripción: {e}")
#                 return redirect('error_page')
#
#             try:
#                 print(f"Ruta del archivo: {audio_file_path}")
#                 text = wc.transcribe_audio(audio_file_path)
#                 print(text)
#                 return redirect('success_page')
#             except Exception as e:
#                 print(f"Error en la transcripción: {e}")
#                 return redirect('error_page')
#     return render(request, 'upload_audio.html')
#

from django.http import JsonResponse


def upload_audio(request):
    temp_audio_file = None  # Initialize temp_audio_file outside the try block

    try:
        audio_file = request.FILES.get('audio_file')

        if not audio_file:
            raise SuspiciousOperation('Archivo de audio no recibido en la solicitud')

        # Crear un archivo temporal para el audio
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_audio_file = temp_file.name  # Assign the file name to temp_audio_file
            for chunk in audio_file.chunks():
                temp_file.write(chunk)

        try:
            wc = WhisperClient()
            text = wc.transcribe_audio(temp_audio_file)
            return JsonResponse({'success': True, 'transcription': text})

        except Exception as e:
            wc = WhisperClient()
            text = wc.transcribe_audio("audio2023")
            print("Text generated: ", text)
            raise SuspiciousOperation(f'Error en la transcripción: {e}')

    except SuspiciousOperation as e:
        wc = WhisperClient()
        text = wc.transcribe_audio("audio2023")
        print("Text generated: ", text)
        return JsonResponse({'success': False, 'error': str(e)})

    except Exception as e:
        print(f"Error no manejado: {e}")

        return JsonResponse({'success': False, 'error': 'Error interno del servidor'})

    finally:
        if temp_audio_file:
            os.remove(temp_audio_file)


def upload_audio_page(request):
    return render(request, 'upload_audio.html')


def success_page(request):
    return render(request, 'success_page.html')


def error_page(request):
    return render(request, 'error_page.html')
