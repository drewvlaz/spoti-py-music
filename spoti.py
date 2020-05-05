from __future__ import unicode_literals
import youtube_dl
import eyed3

class Song:
    """ Contains and controls song elements """

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def download(self):
        """ Downloads mp3 from youtube """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './songs/' + self.title + '.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }]
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=fHI8X4OXluQ'])

    def get_URL(self):
        pass

    def edit_metadata(self):
        audiofile = eyed3.load('./songs/' + self.title + '.mp3')
        audiofile.tag.artist = self.artist
        audiofile.tag.title = self.title
        audiofile.tag.save()


def main():
    new_song = Song("Blinding Lights", "The Weeknd")
    new_song.download()
    new_song.edit_metadata()


main()
