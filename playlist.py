from secrets import SPOTIFY_TOKEN

import requests
from song import Song

class Playlist:
    """ Contains and controls playlist elements """

    def __init__(self, name, playlist_id):
        self.name = name
        self.id = playlist_id

    def get_playlist(self):
        """ Get playlist data from spotify """
        query = f'https://api.spotify.com/v1/playlists/{self.id}/tracks'
        # NOTE: Auth token expires every hour
        # TODO: Set up auth workflow to get around this
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
        """ Download each song in the playlist """
        for i in range(42,len(self.data.json()['items'])):
            if i > 50:
                break

            # Get song data
            title = self.data.json()['items'][i]['track']['name']
            artist = self.data.json()['items'][i]['track']['album']['artists'][0]['name']
            cover_art = requests.get(self.data.json()['items'][i]['track']['album']['images'][0]['url']).content

            # Initialize song obj and download
            song = Song(title, artist, cover_art, self.name)
            song.download()
