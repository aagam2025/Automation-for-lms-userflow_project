from pages.course_page import CoursePage
from config.config import LOGIN_EMAIL, LOGIN_PASSWORD


def test_course_flow(page):
    course = CoursePage(page)

    # Step 1: Login
    course.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert "login" not in page.url.lower(), "Login failed"

    # Step 2: Go to courses
    course.navigate_to_courses()
    assert "course" in page.url.lower(), "Did not reach courses page"

    # Step 3: Search a course
    course.search_course("test_inf")

    # Step 4: Verify results exist
    rows = page.locator("table tbody tr")
    assert rows.count() > 0, "No courses found in search"
