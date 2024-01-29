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
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')

        if audio_file:
            try:
                # Guarda el archivo localmente
                audio_file_path = f"audio_temp/{audio_file.name}"
                with open(audio_file_path, 'wb') as audio_file_local:
                    for chunk in audio_file.chunks():
                        audio_file_local.write(chunk)

                # Transcribe el audio con Whisper
                wc = WhisperClient()

                # Realiza la transcripción y devuelve el texto
                text = wc.transcribe_audio(audio_file_path)

                return JsonResponse({'success': True, 'transcription': text})
            except Exception as e:
                print(f"Error en la transcripción: {e}")

                return JsonResponse({'success': False, 'error': str(e)})
        else:
            wc = WhisperClient()

            # Realiza la transcripción y devuelve el texto
            text = wc.transcribe_audio("audio_2023062")
            print("Texto generad0,", text)
            return JsonResponse({'success': False, 'error': 'Archivo de audio no recibido en la solicitud'})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})


def upload_audio_page(request):
    return render(request, 'upload_audio.html')


def success_page(request):
    return render(request, 'success_page.html')


def error_page(request):
    return render(request, 'error_page.html')
