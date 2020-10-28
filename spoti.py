from playlist import Playlist


def main():
    playlists = {
        "Just Good Music": '37i9dQZF1DX0b1hHYQtJjp',
        "Today\'s Top Hits": '37i9dQZF1DXcBWIGoYBM5M',
        "Power Workout": '37i9dQZF1DWUVpAXiEPK8P',
        "Hot Rhythmic": '37i9dQZF1DWYs83FtTMQFw',
        "Rap Caviar": '37i9dQZF1DX0XUsuxWHRQd',
        "late nite - sad times": '7IeEWVi4eLAYGhz4Aj0hpp',
        "2000s Throwbacks": '5tW8T4fK7DoTtLr8ordLpa'
    }

    selection = "late nite"
    pl = Playlist(selection, playlists[selection])
    pl.get_playlist()
    pl.download_songs()


main()
