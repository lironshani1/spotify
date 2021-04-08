import pytest
from Logic import user_logic
from urllib.parse import urljoin


class Test_user:
    def test_sign_up_same_id(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r2 = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name="lironshani")
        if "error" not in r2.text:
            r = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
            print(r.text)
            assert "error" in r.text
        else:
            assert False

    @pytest.mark.parametrize("sign_up_test_case", ["sign_up_no_password", "sign_up_no_user_name", "sign_up_user_name_integer", "sign_up_password_integer", "sign_up_empty_name", "sign_up_empty_password"])
    def test_sign_up(self, get_url, get_tests_data, sign_up_test_case):
        r = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data[sign_up_test_case])
        assert not r.ok

    def test_add_friend_success(self, get_url, get_tests_data):
        user_logic.add_friend(url=urljoin(get_url, "/users/add_friend"), json=get_tests_data["add_friend_success"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["add_friend_success"]["user_name"])
        assert r.ok

    def test_add_friend_no_password(self, get_url, get_tests_data):
        r = user_logic.add_friend(url=urljoin(get_url, "/users/add_friend"), json=get_tests_data["add_friend_no_password"])
        assert not r.ok

    def test_add_friend_wrong_password(self, get_url, get_tests_data):
        r = user_logic.add_friend(url=urljoin(get_url, "/users/add_friend"), json=get_tests_data["add_friend_wrong_password"])
        print(r.text)
        assert "error" in r.text

    @pytest.mark.parametrize("add_friend_test_case", ["add_friend_same_user", "add_friend_not_exist"])
    def test_add_friend_fail(self, get_url, get_tests_data, add_friend_test_case):
        r = user_logic.add_friend(url=urljoin(get_url, "/users/add_friend"), json=get_tests_data[add_friend_test_case])
        assert not r.ok

    def test_add_playlist_success(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_success"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user"]["user_name"])
        assert get_tests_data["add_playlist_success"]["playlist_name"] in r.json()["data"]["playlists"]

    def test_add_playlist_no_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_no_password"])
        assert not r.ok

    def test_add_playlist_twice(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r1 = user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user"]["user_name"])
        if get_tests_data["add_playlist"]["playlist_name"] in r.json()["data"]["playlists"]:
            r = user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist"])
            assert "error" in r.text

    def test_add_playlist_different_users(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user2"])
        user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist"])
        user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist2"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user2"]["user_name"])
        assert get_tests_data["add_playlist2"]["playlist_name"] in r.json()["data"]["playlists"]

    def test_dont_show_password(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user"]["user_name"])
        print(r.text)
        assert "password" not in r.text

    def test_change_password_success(self, get_url, get_tests_data):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        user_logic.change_password(url=urljoin(get_url, "/users/change_password"), json=get_tests_data["change_password_success"])
        user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_new_password"])
        r = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name=get_tests_data["new_user"]["user_name"])
        print(r.text)
        assert get_tests_data["add_playlist_new_password"]["playlist_name"] in r.json()["data"]["playlists"]

    @pytest.mark.parametrize("change_password_test_case", ["change_password_wrong_password", "change_password_empty"])
    def test_change_password_wrong_password(self, get_url, get_tests_data, change_password_test_case):
        user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        r = user_logic.change_password(url=urljoin(get_url, "/users/change_password"), json=get_tests_data[change_password_test_case])
        assert "error" in r.text


