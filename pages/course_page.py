from pages.base_page import BasePage

class CoursePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, mail: str, password: str) -> None:
        self.fill("#email", mail)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()

    def navigate_to_courses(self) -> None:
        self.page.get_by_role("link", name="Courses ").click()
        self.page.get_by_role("link", name="List Courses").click()
        self.wait_for_network()

    def search_course(self, course_name: str) -> None:
        self.page.get_by_role("textbox", name="Search By Title or Ref").fill(course_name)
        self.page.get_by_role("textbox", name="Search By Title or Ref").press("Enter")
        self.wait_for_network()

    def add_course(self, course_ref: str, title: str, file_path: str) -> None:
        self.page.get_by_role("link", name=" Add Course").click()
        self.wait_for_network()
        self.page.locator("select[name=\"Format\"]").select_option("XAPI")
        self.page.locator("input[name=\"CourseRef\"]").fill(course_ref)
        self.page.get_by_role("button", name="Choose File").set_input_files(file_path)
        self.page.locator("input[name=\"Title\"]").fill(title)
        self.page.locator("#AllowedAttempts").select_option("3")
        self.page.locator(".input-group-addon").click()
        self.page.locator("body").press("Enter")
        self.page.get_by_role("button", name="Save", exact=True).click()
        self.wait_for_network()