from __future__ import unicode_literals
import youtube_dl

#Given a URL, uses YoutubeDL to download the subtitles of a speech in dfxp format. Call by passing a url and specify the path in which to store the file. 
def DownloadSpeech(url,filename):
    class MyLogger(object):
        def debug(self, msg):
            print(msg)

        def warning(self, msg):
            print(msg)

        def error(self, msg):
            print(msg)


    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    outputName = 'data/' + filename
    ydl_opts = {
        'logger': MyLogger(),
        'writesubtitles': True,
        'skip_download': True,
        'outtmpl': outputName
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

DownloadSpeech('http://www.c-span.org/video/?326471-1/hillary-clinton-presidential-campaign-announcement','TestSpeech')