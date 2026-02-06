from pages.login_page import LoginPage
from pages.add_course_page import Add_Course
from config.config import *

class TestAddCourse:
    def test_add_course(self, page):
        # Step 1: Login
        login_page = LoginPage(page)
        login_page.login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower(), "Login failed"
        

        # Step 2: Navigate to courses
        add_course = Add_Course(page)
        add_course.navigate_to_courses()
        assert "course" in page.url.lower(), "Did not reach courses page"

        # Step 3: Add a course
        add_course.add_course()

        # # Step 4: Verify course was added (this is a placeholder, adjust as needed)
        # course_exists = page.locator("text=Tt_course").is_visible()
        # assert course_exists, "Course was not added successfully"

