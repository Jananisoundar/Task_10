from typing import List, Dict
import random


class Audio:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating: int):
        self.ratings.append(rating)

    def average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)


class Playlist:
    def __init__(self, name: str, genre: str):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio: Audio):
        self.audios.append(audio)

    def search_audio(self, name: str) -> List[Audio]:
        return [audio for audio in self.audios if name.lower() in audio.name.lower()]

    def add_rating(self, rating: int):
        self.ratings.append(rating)

    def average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)


class User:
    def __init__(self, name: str):
        self.name = name

    def rate_audio(self, audio: Audio, rating: int):
        audio.add_rating(rating)

    def rate_playlist(self, playlist: Playlist, rating: int):
        playlist.add_rating(rating)


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name: str, genre: str) -> Playlist:
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_playlist(self, name: str) -> List[Playlist]:
        return [playlist for playlist in self.playlists if name.lower() in playlist.name.lower()]

    def generate_random_ratings(self):
        users = [User(f'User{i}') for i in range(1, 4)]
        for playlist in self.playlists:
            for user in users:
                user.rate_playlist(playlist, random.randint(1, 5))
            for audio in playlist.audios:
                for user in users:
                    user.rate_audio(audio, random.randint(1, 5))


# Example usage
if __name__ == "__main__":
    player = MusicPlayer()
    playlist1 = player.create_playlist("Chill Hits", "Chill")
    audio1 = Audio("Chill Vibes", "http://example.com/chillvibes.mp3")
    playlist1.add_audio(audio1)

    player.generate_random_ratings()
    print(f"Average rating for playlist '{playlist1.name}': {playlist1.average_rating()}")
    print(f"Average rating for audio '{audio1.name}': {audio1.average_rating()}")
