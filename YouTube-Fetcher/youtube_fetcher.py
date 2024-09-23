import yt_dlp

def download_youtube_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'progress_hooks': [hook],
        'noplaylist': True, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Get video information
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get('title', None)
        formats = info_dict.get('formats', None)

        # Return video title
        print(f"Title: {video_title}")

        # Display available resolutions
        print("Available resolutions:")
        available_formats = []
        for i, f in enumerate(formats):
            if f.get('height') is not None:
                print(f"{i + 1}. {f['format']} - {f['height']}p")
                available_formats.append(f)

        # Prompt user for resolution
        while True:
            quality_choice = input("Enter the number of the desired resolution (or 'q' to quit): ")
            if quality_choice.lower() == 'q':
                print("Exiting...")
                return
            try:
                index = int(quality_choice) - 1
                if 0 <= index < len(available_formats):
                    selected_format = available_formats[index]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q'.")

        ydl_opts['format'] = selected_format['format_id']

        # Download the selected stream
        print("Downloading video...")
        ydl.download([video_url])
        print(f"Downloaded: {video_title}.mp4")

def hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} - {d['_percent_str']} complete")

if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    download_youtube_video(link)
