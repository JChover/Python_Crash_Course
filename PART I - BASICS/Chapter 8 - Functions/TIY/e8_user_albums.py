# 8-8 User Albums
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

# Create a while loop to allow users to enter album information
while True:
    print("\nPlease enter the artist's name or 'q' to quit:")
    artist_name = input("Artist name: ")
    if artist_name.lower() == 'q':
        break

    print("Please enter the album title or 'q' to quit:")
    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break

    # Call make_album with user inputs and print the resulting dictionary
    album_info = make_album(artist_name, album_title)
    print(album_info)
