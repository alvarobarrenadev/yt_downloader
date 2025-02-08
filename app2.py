# pip install yt_dlp

import os
import re
import yt_dlp

def limpiar_nombre_archivo(nombre):
    """Limpia caracteres no válidos para nombres de archivos."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_audio(url):
    """
    Descarga el audio de un video dado su URL (YouTube/TikTok).
    Guarda el audio con el título original del video.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        titulo = info_dict.get('title', 'audio_descargado')
        titulo_limpio = limpiar_nombre_archivo(titulo)
    
    audio_path = f"{titulo_limpio}.mp3"
    return audio_path, titulo_limpio

def descargar_video(url):
    """
    Descarga el video en formato MP4 con la mejor calidad posible.
    Guarda el archivo con el título original del video.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4' # Fuerza la conversión a MP4 si es necesario
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        titulo = info_dict.get('title', 'video_descargado')
        titulo_limpio = limpiar_nombre_archivo(titulo)
    
    video_path = f"{titulo_limpio}.mp4"
    return video_path, titulo_limpio

def main():
    urls = [
        "",
    ]

    for idx, url in enumerate(urls, start=1):
        try:
            print(f"\nProcesando URL {idx}: {url}")

            # Preguntar al usuario qué desea descargar
            while True:
                opcion = input("¿Qué quieres descargar? (1: Audio, 2: Video, 3: Ambos): ").strip()
                if opcion in ["1", "2", "3"]:
                    break
                print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

            if opcion in ["1", "3"]:
                archivo_audio, titulo_audio = descargar_audio(url)
                print(f"Audio descargado correctamente: {archivo_audio}")

            if opcion in ["2", "3"]:
                archivo_video, titulo_video = descargar_video(url)
                print(f"Video descargado correctamente: {archivo_video}")

        except yt_dlp.utils.DownloadError:
            print(f"Error al descargar el video {idx}. Verifica la URL: {url}")
        except Exception as e:
            print(f"Ocurrió un error inesperado con el video {idx}: {e}")

if __name__ == "__main__":
    main()