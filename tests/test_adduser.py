# from pages.course_page import CoursePage
# from config.config import LOGIN_EMAIL, LOGIN_PASSWORD
from pages.add_user import Add_User
from config.config import *

def test_add_user(page):
    add_user = Add_User(page)

    # Step 1: Login
    add_user.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    assert "login" not in page.url.lower(), "Login failed"

    # Step 2: Go to users
    add_user.go_to_users_list()
    assert "user" in page.url.lower(), "Did not reach users page"

    # Step 3: Add a user
    add_user.add_user(USER_NAME, USEREMAIL)

    # Step 4: Verify user was added (this is a placeholder, adjust as needed)
    user_exists = page.locator(f"text={USEREMAIL}").is_visible()
    assert user_exists, "User was not added successfully"

# def test_course_flow(page):
#     course = CoursePage(page)

   