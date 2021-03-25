from Infra.REST import *


def post_song(url, data=None, json=None, headers=None):
    r = improved_post(url, data, json, headers)
    return r


def get_songs_by_rating_equal(url, rating):
    songs_list = []
    query = {"rank": rating, "op": "eq"}
    r = improved_get(url, query)
    return r


def get_songs_by_rating_less(url, rating):
    songs_list = []
    query = {"rank": rating, "op": "less"}
    r = improved_get(url, query)
    return r


def get_songs_by_rating_greater(url, rating):
    songs_list = []
    query = {"rank": rating, "op": "greater"}
    r = improved_get(url, query)
    list.append(r)
    return songs_list


def get_songs_list(url):
    songs_list = []
    r = get_songs_by_rating_equal(url, 10)
    songs_list.append(r)
    r = get_songs_by_rating_less(url, 10)
    songs_list.append(r)
    r = get_songs_by_rating_greater(url, 10)
    songs_list.append(r)
    return songs_list

