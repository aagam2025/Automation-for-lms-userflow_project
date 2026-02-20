from pages.login_page import LoginPage
from pages.course_assign_page import CourseAssignPage
from config.config import LOGIN_EMAIL, LOGIN_PASSWORD, USER_NAME_1


class TestCourseAssign:
    def test_course_assign(self, page):
        LoginPage(page).login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower(), "Login failed"

        course_assign = CourseAssignPage(page)
        course_assign.assign_course_to_user(USER_NAME_1)

        is_assigned = course_assign.verify_course_assigned(USER_NAME_1)
        assert is_assigned, "Course was not assigned successfully"

        assignment_exists = page.locator(f"text={USER_NAME_1}").is_visible()
        assert assignment_exists, "Course was not assigned successfully"
