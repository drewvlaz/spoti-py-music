from __future__ import unicode_literals
from song import Song


def main():
    new_song = Song("Blinding Lights", "The Weeknd")
    #new_song = Song("Circles", "Post Malone")
    new_song.download()
    new_song.edit_metadata()


main()
