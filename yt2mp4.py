import yt_dlp

def download_highest_quality_video():
    video_url = input("Enter the YouTube video URL: ").strip()
    
    # Lists out options and tells yt-dlp to download the 
    # best availalble video and audio streams separately
    # then merge them. 

    # If separate streams aren's available, it will download
    # the best combined format.
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',     
        'merge_output_format': 'mp4',    # Specifies the merge output should be in MP4 format
        'outtmpl': '%(title)s.%(ext)s',  # Sets the output filename to the video's title with the approp. extension
        'noplaylist': True,              # Ensures that only the single video provided is downloaded, even if the URL us part of a playlist.
    }

    # Save the script to a file with the original name of the vid
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Driver
if __name__ == "__main__":
    download_highest_quality_video()

