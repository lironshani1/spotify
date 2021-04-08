from Infra.REST import *


def add_song_to_playlist(url, data=None, json=None, headers=None):
    r = improved_post(url, data=data, json=json, headers=headers)
    return r
