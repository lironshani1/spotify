from Infra.REST import *


def add_song_to_playlist(url, playlist, song_name, user_name, user_password):
    query = {"playlist_name": playlist, "song_title": song_name, "user_name": user_name, "user_password": user_password}
    r = improved_post(url, query)
    return r
