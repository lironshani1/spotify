from Infra.REST import *


def add_song(url, data=None, json=None, headers=None):
    r = improved_post(url, data, json, headers)
    return r


def get_songs_by_rating_equal(url, rating):
    query = {"rank": rating, "op": "eq"}
    r = improved_get(url, query)
    return r


def get_songs_by_rating_less(url, rating):
    query = {"rank": rating, "op": "less"}
    r = improved_get(url, query)
    return r


def get_songs_by_rating_greater(url, rating):
    query = {"rank": rating, "op": "greater"}
    r = improved_get(url, query)
    return r


def get_songs_list(url):
    songs_list = []
    r = get_songs_by_rating_equal(url, 10).json()
    songs_list.append(r["data"])
    r = get_songs_by_rating_less(url, 10).json()
    songs_list.append(r["data"])
    r = get_songs_by_rating_greater(url, 10).json()
    songs_list.append(r["data"])
    return songs_list


def song_down_vote(url, data=None, json=None):
    r = improved_put(url, data=data, json=json)
    return r


def song_up_vote(url, data=None, json=None):
    r = improved_put(url, data=data, json=json)
    return r