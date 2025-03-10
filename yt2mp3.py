import yt_dlp

def download_audio_as_mp3():
    video_url = input("Enter the YouTube video URL: ").strip()
    
    # Set options to download the best available audio format and then uses ffmpeg to convert it to an MP3 file with a bitrate of 320 kbps. 
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        # Specify the naming template for the downloaded file, using the video's title
        'outtmpl': '%(title)s.%(ext)s',
        # Ensures that only the single video provided is downloaded, even if the URL is part of a playlist
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_audio_as_mp3()

