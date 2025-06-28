# pip install yt_dlp

import re
import yt_dlp

def limpiar_nombre_archivo(nombre: str) -> str:
    """Quita caracteres inválidos para nombres de archivo en Windows/macOS/Linux."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_video(url: str) -> str:
    """
    Descarga el video en MP4 con la mejor calidad posible.
    Devuelve la ruta del archivo guardado.
    """
    ydl_opts = {
        # Vídeo de mayor resolución disponible (MP4) + mejor audio (M4A) y los mezcla.
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  # Fuerza la salida a MP4 si hace falta
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        titulo_limpio = limpiar_nombre_archivo(info.get('title', 'video_descargado'))

    return f'{titulo_limpio}.mp4'

def main():
    # Pega aquí las URLs que quieras descargar. Una por línea.
    urls = [
        "",
    ]

    for idx, url in enumerate(urls, 1):
        try:
            print(f"\n[{idx}/{len(urls)}] Descargando: {url}")
            archivo = descargar_video(url)
            print(f"✅  Guardado como: {archivo}")
        except yt_dlp.utils.DownloadError:
            print(f"❌  URL inválida o problema de descarga -> {url}")
        except Exception as e:
            print(f"❌  Error inesperado ({url}): {e}")

if __name__ == "__main__":
    main()