import pytest
from Logic import song_logic, user_logic
from urllib.parse import urljoin


class Test_song:
    def test_songs_less_10(self, get_url, get_tests_data):
        r1 = song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        print(r1.text)
        r = song_logic.get_songs_by_rating_less(url=urljoin(get_url, "/songs/ranked_songs"), rating=10)
        print(r.text)
        assert get_tests_data["add_song_success"]["song_title"] in r.text

    def test_new_song_rate_0(self, get_url, get_tests_data):
        r = song_logic.add_song(urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r1 = song_logic.get_songs_by_rating_equal(url=urljoin(get_url, "/songs/ranked_songs"), rating=0)
        assert get_tests_data["add_song_success"]["song_title"] in r1.text

    def test_down_vote_less_0(self, get_url, get_tests_data):
        r = song_logic.add_song(urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r1 = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r1 = song_logic.song_down_vote(url=urljoin(get_url, "/songs/downvote"), json=get_tests_data["song_down_vote"])
        r = song_logic.get_songs_by_rating_less(url=urljoin(get_url, "/songs/ranked_songs"), rating=0)
        assert r.json()["data"] == []

