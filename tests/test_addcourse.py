from pages.login_page import LoginPage
from pages.add_course_page import Add_Course
from config.config import *

class TestAddCourse:
    def test_add_course(self, page):
        login_page = LoginPage(page)

        login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower(), "Login failed"
        

        add_course_1 = Add_Course(page)

        add_course_1.navigate_to_courses()
        assert "course" in page.url.lower(), "Did not reach courses page"

        add_course_1.add_course()
