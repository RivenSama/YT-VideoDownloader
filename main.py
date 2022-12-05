from yt_dlp import YoutubeDL
from threading import Thread 
from youtubesearchpython import VideosSearch

def search(term):
    videosSearch = VideosSearch(term, limit = 1)

    return(videosSearch.result()['result'][0]['id'])


def downloader(term):
    try:
        link="https://www.youtube.com/watch?v="+search(term)
        ydlOptions = {"outtmpl" : "[PATH]/%(title)s.mp4",
        'format':'mp4'}
        with YoutubeDL(ydlOptions) as ydl:
            ydl.download(str(link))
    except: pass


def downloadFromFile(file):
    f = open(file,'r')
    for line in f:
        thread = Thread(target=downloader,args=(line,))
        thread.start()

downloadFromFile('[FILE]')
