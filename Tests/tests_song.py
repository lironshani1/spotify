from Logic import song_logic, user_logic
from urllib.parse import urljoin


class Test_song:
    def test_add_song_success(self, get_url, get_tests_data):
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = song_logic.get_songs_list(url=urljoin(get_url, "/songs/ranked_songs"))
        assert get_tests_data["add_song_success"]["song_title"] in r.__str__()

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

    def test_up_vote(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_up_vote"])
        r = song_logic.get_songs_by_rating_greater(url=urljoin(get_url, "/songs/ranked_songs"), rating=0)
        assert get_tests_data["add_song_success"]["song_title"] in r.json()["data"]

    def test_vote_twice(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_up_vote"])
        r = song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_up_vote"])
        print(r.text)
        assert not r.ok

    def test_up_vote_no_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_up_vote_no_password"])
        print(r.text)
        assert not r.ok

    def test_up_vote_wrong_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_up_vote_wrong_password"])
        print(r.text)
        assert "error" in r.text

    def test_down_vote_no_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_down_vote_no_password"])
        assert not r.ok

    def test_down_vote_wrong_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = song_logic.song_up_vote(url=urljoin(get_url, "/songs/upvote"), json=get_tests_data["song_down_vote_wrong_password"])
        assert "error" in r.text