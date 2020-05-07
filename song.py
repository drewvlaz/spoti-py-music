from bs4 import BeautifulSoup
import youtube_dl
import eyed3
import requests

class Song:
    """ Contains and controls song elements """

    def __init__(self, title, artist, cover_art, playlist):
        self.title = title
        self.artist = artist
        self.cover_art = cover_art
        self.playlist = playlist

    def download(self):
        """ Download mp3 from youtube """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'./songs/{self.playlist}/{self.title}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }]
            }

        # Download song as mp3
        # Weird error sometimes can't find video to download
        successful_download = False
        count = 0
        while not successful_download and count < 5:
            count += 1
            try:
                # Locate download url
                self.get_URL()
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([self.URL])
                    successful_download = True

            except KeyboardInterrupt:
                raise

            except:
                print("Error in downloading...Retrying")

        # Automatically edit metadata
        self.edit_metadata()

    def get_URL(self):
        """ Locate youtube URL based on title and artist """
        query = 'https://www.youtube.com/results?search_query='
        for word in self.title.split(' '):
            query += word + '+'
        for word in self.artist.split(' '):
            query += word + '+'
        query += 'lyrics'

        search_page = requests.get(query)
        soup = BeautifulSoup(search_page.text, 'html.parser')
        link = soup.find('a', {'class': 'yt-uix-sessionlink spf-link'})

        self.URL = 'https://www.youtube.com/' + link.get('href')
        successful_link = True

    def edit_metadata(self):
        """ Edit title, artist, and album art """
        audiofile = eyed3.load(f'./songs/{self.playlist}/{self.title}.mp3')
        audiofile.tag.artist = self.artist
        audiofile.tag.title = self.title
        # TODO: Album art doesn't display right on phone
        audiofile.tag.images.set(3, self.cover_art, 'image/jpeg', 'Cover art')
        audiofile.tag.save()
