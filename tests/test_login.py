from pages.login_page import LoginPage
from config.config import *

class TestLogin:

    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower()

    def test_invalid_email(self, page):
        login_page = LoginPage(page)
        login_page.login("invalid_email", LOGIN_PASSWORD)
        assert page.locator("#email").is_visible()

    def test_invalid_password(self, page):
        login_page = LoginPage(page)
        login_page.login(LOGIN_EMAIL, "invalid_password")
        assert page.locator("#email").is_visible()

    def test_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.login("", "")
        assert page.locator("#email").is_visible()
