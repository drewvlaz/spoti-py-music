from secrets import CLIENT_ID, CLIENT_SECRET
from song import Song

import requests
import base64
import json

class Playlist:
    """ Contains and controls playlist elements """

    def __init__(self, name, playlist_id):
        self.name = name
        self.id = playlist_id

    def get_auth_token(self):
        """ Get authorization token from client credentials """

        url = 'https://accounts.spotify.com/api/token'

        # Encode to base 64
        # Refer to https://dev.to/mxdws/using-python-with-the-spotify-api-1d02
        message = f"{CLIENT_ID}:{CLIENT_SECRET}"
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')

        r = requests.post(
            url,
            headers={
                'Authorization': f'Basic {base64Message}'
            },
            data={
                'grant_type': 'client_credentials'
            }
        )

        return r.json()['access_token']

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
                'Authorization': f'Bearer {self.get_auth_token()}',
            }
        )

        # print(json.dumps(self.data.json(), indent=2))

    def download_songs(self):
        """ Download each song in the playlist """
        playlist_size = len(self.data.json()['items'])
        for i in range(6,playlist_size):
            if i > 100:
                break

            # Show status
            print(f"\nSong {i}/{playlist_size}")

            # Get song data
            title = self.data.json()['items'][i]['track']['name']
            artist = self.data.json(
            )['items'][i]['track']['album']['artists'][0]['name']
            cover_art = requests.get(
                self.data.json()['items'][i]['track']['album']['images'][0]['url']).content

            # Initialize song obj and download
            song = Song(title, artist, cover_art, self.name)
            song.download()
