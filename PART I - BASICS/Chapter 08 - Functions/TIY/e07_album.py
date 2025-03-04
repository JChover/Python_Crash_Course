# 8-7 Album
def make_album(artist_name, album_title, num_songs=None):
    """
    Builds a dictionary describing a music album.

    Parameters:
    artist_name (str): The name of the artist.
    album_title (str): The title of the album.
    num_songs (int, optional): The number of songs on the album. Defaults to None.

    Returns:
    dict: A dictionary containing the artist name, album title, and optionally the number of songs.
    """
    album_info = {
        'artist': artist_name,
        'title': album_title
    }
    if num_songs is not None:
        album_info['tracks'] = num_songs
    return album_info

# Create three dictionaries representing different albums
album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('Pink Floyd', 'Dark Side of the Moon')
album3 = make_album('Led Zeppelin', 'IV', 8)

# Print each dictionary to show that they are storing the album information correctly
print(album1)
print(album2)
print(album3)
