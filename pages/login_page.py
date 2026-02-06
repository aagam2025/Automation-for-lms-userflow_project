from pages.base_page import BasePage
from config.config import *

class LoginPage(BasePage):

    def open(self):
        self.page.goto(BASE_URL, timeout=6000)
        self.wait_for_network()

    def login(self, email: str, password: str):
        self.page.goto(BASE_URL)
        self.fill("#email", email)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()
