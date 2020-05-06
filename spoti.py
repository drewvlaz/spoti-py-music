from playlist import Playlist

def main():
    playlists = {
        "Just Good Music":'37i9dQZF1DX0b1hHYQtJjp',
        "Today\'s Top Hits":'37i9dQZF1DXcBWIGoYBM5M'
    }

    pl = Playlist('Today\'s Top Hits', playlists['Today\'s Top Hits'])
    pl.get_playlist()
    pl.download_songs()

main()
