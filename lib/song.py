import matplotlib.pyplot as plt 

class Song:
    # class attribute
    count = 0
    artists = []
    genres = []
    genre_count_dict = {}
    artist_count_dict = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_self()
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)
        Song.genre_count(self.genre)
        Song.artist_count(self.artist)
        

    @classmethod
    def add_song_to_self(cls):
        cls.count += 1
    
    @classmethod
    def genre_count(cls, genre):
        if genre not in cls.genre_count_dict:
            cls.genre_count_dict[genre] = 1
        else:
            cls.genre_count_dict[genre] += 1

    @classmethod
    def add_to_genres(cls, genre):
        if not genre in cls.genres:
            cls.genres.append(genre)
            
        else:   
            None
    
    @classmethod
    def artist_count(cls, artist):
        if artist not in cls.artist_count_dict:
            cls.artist_count_dict[artist] = 1
        else:
            cls.artist_count_dict[artist] += 1

    
    @classmethod
    def add_to_artists(cls, artist):
        if not artist in cls.artists:
            cls.artists.append(artist)
        else: 
            None

    @classmethod
    def plot_genre_histogram(cls):
        genres = list(cls.genre_count_dict.keys())
        counts = list(cls.genre_count_dict.values())

        plt.bar(genres, counts)
        plt.xlabel('Genres')
        plt.ylabel('Count')
        plt.title('Genre Count Histogram')
        plt.show()

    @classmethod
    def plot_artist_histogram(cls):
        artists = list(cls.artist_count_dict.keys())
        counts = list(cls.artist_count_dict.values())

        plt.bar(artists, counts)
        plt.xlabel('Artists')
        plt.ylabel('Count')
        plt.title('Artist Count Histogram')
        plt.show()

pop_song = Song('Pop', 'Pop Artist', 'Pop')
pop_song_2 = Song('Pop2', 'Pop Artist', 'Pop')
rock_song = Song('Rock', 'Rock Artist', 'Rock')
country_song = Song('Country', 'Country Artist', 'Country')
country_song2 = Song('Country2', 'Country Artist', 'Country')

print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.genre_count_dict)
print(Song.artist_count_dict)


Song.plot_genre_histogram()
Song.plot_artist_histogram()
    


