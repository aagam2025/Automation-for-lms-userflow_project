from pages.base_page import BasePage
import re
class CourseAssignPage(BasePage):
    course_name_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/a'
    course_list_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/ul/li[1]/a'
    user_btn ='//*[@id="crudTable"]/tbody/tr[1]/td[3]/a'
    users_btn_id = 'base-questionsTab'
    add_user_btn_xpath = '//*[@id="userAssessmentForm"]/i'
    user_selection_placeholder = 'Select users'
    submit_btn_xpath = '//*[@id="newUserAssignmentForm"]/div/div[3]/div/button[2]'

    save_btn_id = 'btn_save'
    profile_btn_xpath = '//*[@id="navbar-mobile"]/ul[2]/li[3]/a'
    logout_btn_xpath = '//*[@id="navbar-mobile"]/ul[2]/li[3]/div/a[3]'
    teams_btn_xpath = '//*[@id="setup-training"]/a'
    users_list_xpath = '//*[@id="setup-training"]/ul/li[1]/a'
    specific_user_xpath = '//*[@id="crudTable"]/tbody/tr[2]/td[2]/span/a'

    def __init__(self, page):
        super().__init__(page)

    def login(self, mail: str, password: str) -> None:
        self.fill("#email", mail)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()

    def assign_course_to_user(self, user_name: str):
        self.page.locator(self.course_name_xpath).click()
        self.page.locator(self.course_list_xpath).click()
        self.wait_for_network()
        self.page.locator(self.user_btn).click()
        self.wait_for_network()
        self.page.locator(f'#{self.users_btn_id}').click()
        self.wait_for_network()
        self.page.locator(self.add_user_btn_xpath).click()
        self.page.locator("span.select2-selection").click()
        self.page.locator("input.select2-search__field").fill(user_name)
        self.page.locator(
            f'li.select2-results__option:text-is("{user_name}")'
        ).click()
        self.page.locator("body").click()
        self.page.locator(self.submit_btn_xpath).click()
        # self.page.locator(f'#{self.save_btn_id}').click()
        self.wait_for_network()

    def verify_course_assigned(self, user_name: str) -> bool:
        self.page.locator(self.teams_btn_xpath).click()
        self.page.locator(self.users_list_xpath).click()
        self.page.locator(self.specific_user_xpath).click()
        self.wait_for_network()
        course_assigned = self.page.locator(f'text={user_name}').is_visible()

        return course_assigned