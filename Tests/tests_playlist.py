from Logic import song_logic, user_logic, playlist_logic
from urllib.parse import urljoin


class Test_playlist:
    def test_add_song_not_exist(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = playlist_logic.add_song_to_playlist(url=urljoin(get_url, "/playlists/add_song"), json=get_tests_data["add_song_to_playlist"])
        print(r.text)
        assert "error" in r.text

    def test_add_song_twice(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        r = playlist_logic.add_song_to_playlist(url=urljoin(get_url, "/playlists/add_song"), json=get_tests_data["add_song_to_playlist"])
        if r.ok:
            r = playlist_logic.add_song_to_playlist(url=urljoin(get_url, "/playlists/add_song"), json=get_tests_data["add_song_to_playlist"])
            print(r.text)
            assert "error" in r.text

    def test_add_song_success(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = song_logic.add_song(url=urljoin(get_url, "/songs/add_song"), json=get_tests_data["add_song_success"])
        user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_success"])
        r = playlist_logic.add_song_to_playlist(url=urljoin(get_url, "/playlists/add_song"), json=get_tests_data["add_song_to_playlist"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user"]["user_name"])
        assert False #cant see the song in the playlist

    def test_delete_song_from_playlist(self):
        assert False
