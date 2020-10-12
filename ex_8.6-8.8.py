# 8.6
def city_country(city, country):
    country_city = f"{city},{country}"
    print(country_city.title())

city_country('rio', 'brazil')
city_country('moscow', 'russia')
city_country('minsk', 'belarus')

# 8.7


def make_album(name_artist, name_album, count_track=''):
    album = {'artist': name_artist, 'album': name_album}
    if count_track:
        album['tracks'] = count_track
    return album


print("\nYou can make music album list!")

while True:
    print("\nMaking album list:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break
    count_track = input("Number of songs: ")
    if count_track == 'q':
        break
    album = make_album(artist_name.title(), album_name.title(), count_track)
    print(f"\n{album}")