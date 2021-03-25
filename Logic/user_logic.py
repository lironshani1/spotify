from Infra.REST import *


def post_user(url, user_name, user_password):
    user_to_post = {"user_name": user_name, "user_password": user_password}
    r = improved_post(url, user_to_post)
    return r


def get_user(url, user_name):
    query = {"user_name": user_name}
    r = improved_get(url, query)
    return r


def add_friend(url, friend_name, user_name, user_password):
    query = {"friend_name": friend_name, "user_name": user_name, "user_password": user_password}
    r = improved_put(url, query)
    return r


def add_playlist(url, playlist_name, user_name, user_password):
    query = {"playlist_name": playlist_name, "user_name": user_name, "user_password": user_password}
    r = improved_post(url, query)
    return r


def change_password(url, user_name, new_pass, user_password):
    query = {"user_name": user_name, "user_new_password": new_pass, "user_password": user_password}
    r = improved_put(url, query)
    return r

