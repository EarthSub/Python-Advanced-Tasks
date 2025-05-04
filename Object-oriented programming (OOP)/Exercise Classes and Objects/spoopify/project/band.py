from project.album import Album


class Band:

    def __init__(self, name: str, ):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_to_remove = next((a for a in self.albums if a.name == album_name), None)
        if not album_to_remove:
            return f"Album {album_name} is not found."
        if album_to_remove.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        result = "\n".join(album.details() for album in self.albums)
        return f"Band {self.name}\n{result}"
