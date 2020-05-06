from __future__ import unicode_literals

import json
import requests
from PIL import Image
from io import BytesIO
from song import Song
from secrets import SPOTIFY_TOKEN

class Playlist:
    def __init__(self, name, playlist_id):
        self.name = name
        self.id = playlist_id

    def get_playlist(self):
        query = f'https://api.spotify.com/v1/playlists/{self.id}/tracks'
        self.data = requests.get(
            query,
            params={
                'fields': 'items(track(album(artists, images), name))'
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {SPOTIFY_TOKEN}',
            }
        )

    def download_songs(self):
        """ Downloads each song in the playlist """
        #for i in range(len(self.data.json()['items'])):
        for i in range(2):
            # Get song data
            title = self.data.json()['items'][i]['track']['name']
            artist = self.data.json()['items'][i]['track']['album']['artists'][0]['name']
            cover_art_raw = requests.get(self.data.json()['items'][0]['track']['album']['images'][0]['url']).content
            cover_art = Image.open(BytesIO(cover_art_raw))

            # Initialize song obj and download
            song = Song(title, artist, cover_art, self.name)
            song.download()
            song.edit_metadata()

def main():
    playlists = {
        'Just Good Music':'37i9dQZF1DX0b1hHYQtJjp'
    }

    pl = Playlist('Just Good Music', playlists['Just Good Music'])
    pl.get_playlist()
    pl.download_songs()

main()
