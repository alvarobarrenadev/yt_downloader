import yt_dlp

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
            print("Descarga completada exitosamente")

    except Exception as e:
        print(f"Hubo un error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    formato = input("¿En qué formato deseas descargar (video/audio)?: ").lower()
    descargar_video_yt(url, formato)