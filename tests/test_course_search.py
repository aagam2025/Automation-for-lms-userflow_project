from pages.course_page import CoursePage
from config.config import LOGIN_EMAIL, LOGIN_PASSWORD


def test_course_flow(page):
    course = CoursePage(page)

    course.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert "login" not in page.url.lower(), "Login failed"

    course.navigate_to_courses()
    assert "course" in page.url.lower(), "Did not reach courses page"

    course.search_course("test_inf")