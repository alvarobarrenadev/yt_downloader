import yt_dlp

def descargar_video_yt_dlp(url, formato='mp4'):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [],
    }

    if formato == 'mp3':
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
    formato = input("¿En qué formato deseas descargar (mp4/mp3)?: ").lower()
    descargar_video_yt_dlp(url, formato)