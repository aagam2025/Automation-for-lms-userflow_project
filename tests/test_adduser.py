from pages.add_user import Add_User
from config.config import *

def test_add_user(page):
    add_user = Add_User(page)

    add_user.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert "login" not in page.url.lower(), "Login failed"

    add_user.go_to_users_list()
    assert "user" in page.url.lower(), "Did not reach users page"

    add_user.add_user(USER_NAME, USEREMAIL)

    user_exists = page.locator(f"text={USEREMAIL}").is_visible()
    assert user_exists, "User was not added successfully"
