from Infra.REST import *
import json


def add_user(url, data=None, json=None, headers={"Content-Type": "application/json"}):
    r = improved_post(url=url, headers=headers, data=data, json=json)
    return r


def get_user(url, user_name):
    query = {"user_name": user_name}
    r = improved_get(url, query)
    return r


def add_friend(url, data=None, json=None):
    r = improved_put(url, data=data, json=json)
    return r


def add_playlist(url, data=None, json=None, headers=None):
    r = improved_post(url, data=data, json=json, headers=headers)
    return r


def change_password(url, data=None, json=None):
    r = improved_put(url, data=data, json=json)
    return r

