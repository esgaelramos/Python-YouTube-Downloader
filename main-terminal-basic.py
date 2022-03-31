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

    url = YouTube(link)
    
    video = url.streams.first()
    
    video.download()

if __name__ == "__main__":
    run()
