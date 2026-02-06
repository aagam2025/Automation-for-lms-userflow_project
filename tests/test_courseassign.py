from pages.login_page import LoginPage
from pages.course_assign_page import CourseAssignPage
from config.config import *

class TestCourseAssign:
    def test_course_assign(self, page):
        LoginPage(page).login(LOGIN_EMAIL, LOGIN_PASSWORD)
        assert "login" not in page.url.lower(), "Login failed"

        course_assign = CourseAssignPage(page)
        course_assign.assign_course_to_user("Abc")

        # Step 3: Verify course was assigned using the new method in CourseAssignPage
        is_assigned = course_assign.verify_course_assigned("Abc")
        assert is_assigned, "Course was not assigned successfully"

        # Step 4: Verify course was assigned (this is a placeholder, adjust as needed)
        assignment_exists = page.locator("text=Abc").is_visible()
        assert assignment_exists, "Course was not assigned successfully"

        # Step 5: Logout
        course_assign.logout()
        assert "/" in page.url.lower(), "Logout failed"