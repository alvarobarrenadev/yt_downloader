import yt_dlp
from concurrent.futures import ThreadPoolExecutor

def descargar_video_yt(url, formato='video'):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [],
    }

    if formato == 'audio':
        opciones['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print(f"Descarga completada exitosamente para: {url}")

    except Exception as e:
        print(f"Hubo un error con {url}: {e}")

def descargar_multiples_videos(urls, formato='video', num_hilos=4):
    print(f"Iniciando descargas en formato: {formato}...")
    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        futures = [executor.submit(descargar_video_yt, url, formato) for url in urls]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Error durante la descarga: {e}")

if __name__ == "__main__":
    urls = [
        ""
    ]

    formato = input("¿En qué formato deseas descargar (video/audio)?: ").lower()
    descargar_multiples_videos(urls, formato, num_hilos=10)