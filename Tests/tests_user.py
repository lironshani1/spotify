import pytest
from Logic import user_logic
from urllib.parse import urljoin


class Test_user:
    def test_sign_up_same_id(self, get_url, get_tests_data):
        r1 = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
        print(r1.text)
        r2 = user_logic.get_user(url=urljoin(get_url, "/users/get_user"), user_name="lironshani")
        if r2.text.find('error') == -1:
            r = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data["new_user"])
            print(r.text)
            assert "error" in r.text

    @pytest.mark.parametrize("sign_up_test_case", ["sign_up_no_password", "sign_up_no_user_name", "sign_up_user_name_integer", "sign_up_password_integer"])
    def test_sign_in(self, get_url, get_tests_data, sign_up_test_case):
        r = user_logic.add_user(url=urljoin(get_url, "/users/add_user"), json=get_tests_data[sign_up_test_case])
        print(r.text)

    def test_add_friend_success(self, get_url, get_tests_data):
        r = user_logic.add_friend(url=urljoin(get_url, "/users/add_friend"), json=get_tests_data["add_friend_success"])
        print(r.status_code)
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
        r = user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_success"])
        assert r.ok

    def test_add_playlist_no_password(self, get_url, get_tests_data):
        r = user_logic.add_playlist(url=urljoin(get_url, "/users/add_playlist"), json=get_tests_data["add_playlist_no_password"])
        assert not r.ok
