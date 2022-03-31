from pytube import YouTube

def run():

    print("""
        Welcome to My YouTube Video Downloader | By DataFlair
        -----------------------------------------------------
        It's simple:
        Only put the link of video and clic!
    """)

    link = input("""
        Put the link: """)

    title_video = input("""
        Put the title video: """)

    url = YouTube(link)
    
    video = url.streams.first() 

    video.download(filename = title_video, output_path = "/home/gael/Documentos/Python/Python-YouTube-Downloader/videos")


if __name__ == "__main__":
    run()
