class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for x in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(int(photos_count * 0.25))

    def add_photo(self, label):
        for row in range(self.pages):
            for col in range(3):
                if len(self.photos[row]) < 4:
                    self.photos[row].append(label)
                    return f"{label} photo added successfully on page {row+1} slot {len(self.photos[row])}"
        return f"No more free spots"

    def display(self):
        token = "-----------\n"
        for x in self.photos:
            tok = []
            for y in range(len(x)):
                tok.append("[]")
            token += f"{' '.join(tok)}"
            token += "\n-----------\n"
        return token




album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())