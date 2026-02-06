from pages.base_page import BasePage
from config.config import *

class Add_Course(BasePage):
    course_btn_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/a'
    list_course_btn_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/ul/li[1]/a'
    add_course_btn_xpath = '//*[@id="btn-group"]/a[2]'
    course_format_dropdown_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[1]/div/div/select'
    ref_input_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[2]/div/div/input'
    title_input_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[3]/div/div/input'
    cancel_btn_xpath = '//*[@id="saveActions"]/a'
    date_xpath = "/html/body/div[4]/div[1]/table/tbody/tr[2]/td[5]"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_courses(self):
        self.click(self.course_btn_xpath)
        self.click(self.list_course_btn_xpath)
        self.wait_for_network()


    def add_course(self):
        self.click(self.add_course_btn_xpath)
        self.page.wait_for_timeout(5000)

        self.click(self.course_format_dropdown_xpath)
        self.page.locator(self.course_format_dropdown_xpath).select_option(label="XAPI")
        
        self.fill(self.ref_input_xpath, "Tt_course")
        self.fill(self.title_input_xpath, "Tt_course")
        
        self.page.click("#content_updated_at")
        self.page.wait_for_timeout(2000)
        self.page.click(f"xpath={self.date_xpath}")
        self.page.wait_for_timeout(2000)
        
        self.page.locator("#AllowedAttempts").select_option("3")
        
        self.page.wait_for_timeout(2000)
        self.page.locator("#Package_file_input").set_input_files(r"C:\Users\Aagam Desai\Downloads\Infosec Course (2).zip")
        self.page.wait_for_timeout(3000)
        
        self.page.locator("#btn_save").click(no_wait_after=True)
        self.wait_for_network()