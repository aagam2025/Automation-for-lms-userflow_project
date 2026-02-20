from pages.login_page import LoginPage
from pages.add_course_page import Add_Course
from config.config import (
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    COURSE_FORMAT,
    COURSE_REF,
    COURSE_TITLE,
    COURSE_ATTEMPTS,
    COURSE_FILE_PATH
)


class TestAddCourse:
    def test_add_course(self, page):
        login_page = LoginPage(page)

        login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower(), "Login failed"
        

        add_course_1 = Add_Course(page)

        add_course_1.navigate_to_courses()
        assert "course" in page.url.lower(), "Did not reach courses page"

        add_course_1.add_course(
            course_format=COURSE_FORMAT,
            course_ref=COURSE_REF,
            course_title=COURSE_TITLE,
            attempts=COURSE_ATTEMPTS,
            file_path=COURSE_FILE_PATH
        )