from project.song import Song


class Album:

    def __init__(self, name: str):
        self.name = name
        self.songs = []
        self.published = False

    def add_song(self, new_song: Song):
        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        elif new_song.name in [x.name for x in self.songs]:
            return f"Song is already in the album."
        self.songs.append(new_song)
        return f"Song {new_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [song.name for song in self.songs]:
            return f"Song is not in the album."
        elif self.published:
            return f"Cannot remove songs. Album is published."
        song = [song for song in self.songs if song.name == song_name][0]
        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        token = f"Album {self.name}\n"
        for tok in self.songs:
            token += '==' + tok.get_info() + '\n'
        return token
