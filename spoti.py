from playlist import Playlist

def main():
    playlists = {
        "Just Good Music":'37i9dQZF1DX0b1hHYQtJjp',
        "Today\'s Top Hits":'37i9dQZF1DXcBWIGoYBM5M',
        "Power Workout":'37i9dQZF1DWUVpAXiEPK8P',
        "Hot Rhythmic":'37i9dQZF1DWYs83FtTMQFw'
    }

    selection = "Hot Rhythmic"
    pl = Playlist(selection, playlists[selection])
    pl.get_playlist()
    pl.download_songs()

main()
