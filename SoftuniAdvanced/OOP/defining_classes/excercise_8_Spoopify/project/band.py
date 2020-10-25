from project.album import Album
from project.song import Song


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_list = [a for a in self.albums if a.name == album_name]
        if not album_list:
            return f"Album {album_name} is not found."
        album = album_list[0]
        if album.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        token = f"Band {self.name}\n"
        for album in self.albums:
            token += album.details() + "\n"
        return token
