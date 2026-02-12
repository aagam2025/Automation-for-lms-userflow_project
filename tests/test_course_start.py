from config.config import *
from pages.course_start import CourseStartPage

# COURSE_START_XPATH = '//*[@id="collapse_Folder37"]/div/div[4]/div[2]/div[1]/a'

class TestCourseStart:

    def test_course_start(self, page):
        course = CourseStartPage(page)
        
        course.login(LOGIN_EMAIL_1, LOGIN_PASSWORD_1)
        assert "login" not in page.url.lower(), "Login failed"

        course.navigate_to_courses_list()

        # course.click_start_on_course(COURSE_START_XPATH)

        page.wait_for_timeout(5000)
        course.click_start_if_visible()

        course.open_course_player(COURSE_ID)
        page.wait_for_timeout(5000)