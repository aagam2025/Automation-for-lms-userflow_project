from pages.base_page import BasePage
import re

class CourseStartPage(BasePage):
    COURSES_MENU_XPATH = '//*[@id="main-menu-navigation"]/li[2]/a'
    course_start_btn_xpath = '//*[@id="cert-download"]/div[2]/div[1]/a'
    start_course_xpath = '//*[@id="cover"]/header/div/div[1]/div/a'

    def __init__(self, page):
        super().__init__(page)

    def login(self, mail: str, password: str) -> None:
        self.fill("#email", mail)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()

    
    def navigate_to_courses_list(self):
        courses_link = self.page.locator(self.COURSES_MENU_XPATH)
        courses_link.wait_for(state="visible", timeout=20000)
        courses_link.click()

        self.page.wait_for_load_state("networkidle", timeout=60000)

        btn_start = self.page.locator(self.course_start_btn_xpath)
        btn_start.wait_for(state="visible", timeout=20000)

        # Wrap the SAME button click in expect_popup
        with self.page.expect_popup() as page1_info:
            btn_start.click()

        page1 = page1_info.value
        page1.wait_for_load_state("domcontentloaded")   # first stage
        page1.wait_for_load_state("networkidle")        # full load
        
        page1.wait_for_selector('iframe[name="SCO"]', timeout=60000)

        sco_frame = page1.frame_locator('iframe[name="SCO"]')

        sco_frame.get_by_role("link", name="START COURSE").wait_for(state="visible", timeout=60000)
        sco_frame.get_by_role("link", name="START COURSE").click()
        