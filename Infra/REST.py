import requests


def improved_get(url, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers)
    return response


def improved_post(url, data=None, json=None, headers=None):
    response = requests.get(url, data=data, json=json, headers=headers)
    return response


def improved_delete(url, params=None):
    response = requests.delete(url, params=params)
    return response


def improved_put(url, data=None):
    response = requests.put(url, data=data)
    return response
