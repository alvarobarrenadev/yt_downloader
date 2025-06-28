# pip install yt_dlp

import re
import yt_dlp

def limpiar_nombre_archivo(nombre: str) -> str:
    """Quita caracteres no válidos para nombres de archivo."""
    return re.sub(r'[\\/*?:"<>|]', "", nombre)

def descargar_audio(url: str) -> str:
    """
    Descarga el audio en MP3 (192 kbps) usando la mejor pista disponible.
    Devuelve la ruta del archivo guardado.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',   # usa el título original
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        titulo_limpio = limpiar_nombre_archivo(info.get('title', 'audio_descargado'))

    return f'{titulo_limpio}.mp3'

def main():
    # Añade aquí tus enlaces. Uno por línea.
    urls = [
        "",
    ]

    for idx, url in enumerate(urls, 1):
        try:
            print(f"\n[{idx}/{len(urls)}] Descargando audio de: {url}")
            archivo = descargar_audio(url)
            print(f"✅  Guardado como: {archivo}")
        except yt_dlp.utils.DownloadError:
            print(f"❌  URL inválida o problema de descarga -> {url}")
        except Exception as e:
            print(f"❌  Error inesperado ({url}): {e}")

if __name__ == "__main__":
    main()
