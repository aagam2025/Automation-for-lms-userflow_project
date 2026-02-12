from pages.base_page import BasePage
from config.config import BASE_URL


class CourseStartPage(BasePage):
    COURSES_MENU_XPATH = '//*[@id="main-menu-navigation"]/li[2]/a'

    CONTENT_WAIT_MS = 2000
    MAX_NAV_STEPS = 200
    AUDIO_POLL_INTERVAL_MS = 1000

    def __init__(self, page):
        super().__init__(page)

    def login(self, mail: str, password: str) -> None:
        self.fill("#email", mail)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()

    def navigate_to_courses_list(self):
        self.page.goto(f"{BASE_URL}dashboard")
        self.wait_for_network()
        courses_link = self.page.locator(self.COURSES_MENU_XPATH)
        courses_link.wait_for(state="visible", timeout=10000)
        courses_link.click()
        self.wait_for_network()

    def click_start_on_course(self, course_start_xpath: str):
        start_btn = self.page.locator(course_start_xpath)
        start_btn.wait_for(state="visible", timeout=15000)
        start_btn.click()
        self.wait_for_network()

    def open_course_player(self, course_id: int):
        url = f"{BASE_URL}local/courses/{course_id}/index.html"
        self.page.goto(url)
        self.wait_for_network()

    def click_start_if_visible(self):
        for name in ("Start", "Start Course", "Begin", "Resume"):
            btn = self.page.get_by_role("button", name=name)
            if btn.count() > 0 and btn.first.is_visible():
                btn.first.click()
                self.page.wait_for_timeout(self.CONTENT_WAIT_MS)
                return True
        return False

    