from pages.base_page import BasePage
from config.config import USER_NAME_1

class Add_User(BasePage):


    team_xpath = '//*[@id="setup-training"]/a'
    users_list_xpath = '//*[@id="setup-training"]/ul/li[1]/a'
    add_user_btn_xpath = '//*[@id="btn-group"]/a'
    name_btn_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[2]/div/div[2]/div/div/input'
    email_id_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[2]/div/div[5]/div/div/input'
    manager_roles_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[2]/div/div[14]/div/div/div/span/span[1]/span/ul/li/input'
    user_roles_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[2]/div/div[15]/div[1]/div'
    save_btn_id = 'btn_save'
    cancel_btn_xpath = '//*[@id="saveActions"]/a'
    records_per_page_xpath = '//*[@id="crudTable_length"]/label/select'
    

    def __init__(self, page):
        super().__init__(page)

    def login(self, mail: str, password: str) -> None:
        self.fill("#email", mail)
        self.fill("#password-field", password)
        self.page.get_by_role("button", name="Sign In with Mail").click()
        self.wait_for_network()

    def go_to_users_list(self):
        self.page.locator(self.team_xpath).click()
        self.page.locator(self.users_list_xpath).click()
        self.wait_for_network()
    
    def add_user(self, name: str, email: str):
        self.page.locator(self.add_user_btn_xpath).click()
        self.page.locator(self.name_btn_xpath).fill(name)
        self.page.locator(self.email_id_xpath).fill(email)
        self.page.locator(self.manager_roles_xpath).click()
        self.page.locator(f'li:has-text("{USER_NAME_1}")').click()


        self.page.locator(f'#{self.save_btn_id}').click()
        cancel_btn = self.page.locator(self.cancel_btn_xpath)
        if cancel_btn.is_visible():
            cancel_btn.click()
        self.wait_for_network()
        self.page.locator('input#text-filter-name').fill(name)
        self.wait_for_network()
        self.page.locator(self.records_per_page_xpath).select_option('100')
        self.wait_for_network()
