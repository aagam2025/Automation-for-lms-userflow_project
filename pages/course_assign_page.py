from pages.base_page import BasePage

class CourseAssignPage(BasePage):
    course_name_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/a'
    course_list_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/ul/li[1]/a'
    user_btn ='//*[@id="crudTable"]/tbody/tr[1]/td[3]/a'
    users_btn_id = 'base-questionsTab'
    add_user_btn_xpath = '//*[@id="userAssessmentForm"]/i'
    user_selection_placeholder = 'Select users'
    # mandatory_btn_id = 'IsMandatory'
    submit_btn_xpath = '//*[@id="newUserAssignmentForm"]/div/div[3]/div/button[2]'
    save_btn_id = 'btn_save'
    profile_btn_xpath = '//*[@id="navbar-mobile"]/ul[2]/li[3]/a'
    logout_btn_xpath = '//*[@id="navbar-mobile"]/ul[2]/li[3]/div/a[3]'
    teams_btn_xpath = '//*[@id="setup-training"]/a'
    users_list_xpath = '//*[@id="setup-training"]/ul/li[1]/a'
    specific_user_xpath = '//*[@id="crudTable"]/tbody/tr[1]/td[2]/span/a'

    def __init__(self, page):
        super().__init__(page)

    # Methods to interact with the course assignment page would go here
    def assign_course_to_user(self, user_name: str):
        self.page.locator(self.course_name_xpath).click()
        self.page.locator(self.course_list_xpath).click()
        self.wait_for_network()
        self.page.locator(self.user_btn).click()
        self.wait_for_network()
        self.page.locator(f'#{self.users_btn_id}').click()
        self.wait_for_network()
        self.page.locator(self.add_user_btn_xpath).click()
        self.page.locator(f'input[placeholder="{self.user_selection_placeholder}"]').fill(user_name)
        self.page.locator(f'text={user_name}').click()
        # self.page.locator(f'#{self.mandatory_btn_id}').click()
        self.page.locator(self.submit_btn_xpath).click()
        self.page.locator(f'#{self.save_btn_id}').click()
        self.wait_for_network()

    def verify_course_assigned(self, user_name: str) -> bool:
        self.page.locator(self.teams_btn_xpath).click()
        self.page.locator(self.users_list_xpath).click()
        self.page.locator(self.specific_user_xpath).click()
        self.wait_for_network()
        # Check if the course is listed for the user
        course_assigned = self.page.locator(f'text={user_name}').is_visible()
        return course_assigned
        
    
    def logout(self):
        self.page.locator(self.profile_btn_xpath).click()
        self.page.locator(self.logout_btn_xpath).click()
        self.wait_for_network()


# Course Assign:
# Click on Course_name using xpath:
# //*[@id="crudTable"]/tbody/tr[1]/td[3]/a
# Id of users button:
# base-questionsTab
# Id of users "+" button:
# userAssessmentForm
# Placeholder of selction of user:
# Select users
# Value:
# Abc
# Mandatory radio button id:
# IsMandatory
# Submit button xpath:
# //*[@id="newUserAssignmentForm"]/div/div[3]/div/button[2]
# Then click on save btn:
# btn_save
# Click on aagam profile btn:
# //*[@id="navbar-mobile"]/ul[2]/li[3]/a
# Click on Logout button:
# //*[@id="navbar-mobile"]/ul[2]/li[3]/div/a[3]

# Verification course assigned or not
# Click on Team dropdown: //*[@id="setup-training"]/a
# Click on Users: //*[@id="setup-training"]/ul/li[1]/a
# Click on Abc user: //*[@id="crudTable"]/tbody/tr[1]/td[2]/span/a