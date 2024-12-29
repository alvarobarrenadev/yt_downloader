import yt_dlp

def descargar__multiples_videos_yt(url, formato='video'):
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

if __name__ == "__main__":
    urls = [
        "",
    ]
    formato = input("¿En qué formato deseas descargar (video/audio)?: ").lower()
    for url in urls:
        descargar__multiples_videos_yt(url, formato)