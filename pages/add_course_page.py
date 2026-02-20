import os
from pathlib import Path

from pages.base_page import BasePage
from config.config import (
    SHORT_TIMEOUT_MS,
    UPLOAD_TIMEOUT_MS,
    COURSE_FORMAT,
    COURSE_REF,
    COURSE_TITLE,
    COURSE_ATTEMPTS,
    COURSE_FILE_PATH
)

class Add_Course(BasePage):
    course_btn_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/a'
    list_course_btn_xpath = '//*[@id="main-menu-navigation"]/li[1]/ul/li[5]/ul/li[1]/a'
    add_course_btn_xpath = '//*[@id="btn-group"]/a[2]'
    course_format_dropdown_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[1]/div/div/select'
    ref_input_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[2]/div/div/input'
    title_input_xpath = '//*[@id="main-wrapper"]/div[3]/div/div[2]/div/form/div/div[1]/div/div[3]/div/div/input'
    cancel_btn_xpath = '//*[@id="saveActions"]/a'
    date_xpath = "/html/body/div[4]/div[1]/table/tbody/tr[4]/td[6]"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_courses(self):
        self.click(self.course_btn_xpath)
        self.click(self.list_course_btn_xpath)
        self.wait_for_network()


    def add_course(self, course_format: str | None = None, course_ref: str | None = None, 
                   course_title: str | None = None, attempts: str | None = None, 
                   file_path: str | None = None):
        # Use config values as defaults if parameters not provided
        if course_format is None:
            course_format = COURSE_FORMAT
        if course_ref is None:
            course_ref = COURSE_REF
        if course_title is None:
            course_title = COURSE_TITLE
        if attempts is None:
            attempts = COURSE_ATTEMPTS
        if file_path is None:
            file_path = COURSE_FILE_PATH
        
        self.click(self.add_course_btn_xpath)
        self.page.wait_for_timeout(SHORT_TIMEOUT_MS)

        self.click(self.course_format_dropdown_xpath)
        self.page.locator(self.course_format_dropdown_xpath).select_option(label=course_format)
        
        self.fill(self.ref_input_xpath, course_ref)
        self.fill(self.title_input_xpath, course_title)
        
        self.page.click("#content_updated_at")
        self.page.wait_for_timeout(SHORT_TIMEOUT_MS)
        self.page.click(f"xpath={self.date_xpath}")
        self.page.wait_for_timeout(SHORT_TIMEOUT_MS)
        
        self.page.locator("#AllowedAttempts").select_option(attempts)
        
        self.page.wait_for_timeout(SHORT_TIMEOUT_MS)
        self.page.locator("#Package_file_input").set_input_files(file_path)
        self.page.wait_for_timeout(UPLOAD_TIMEOUT_MS)
        
        btn = self.page.locator("#btn_save")
        btn.scroll_into_view_if_needed()
        btn.click(timeout=90000)
        # self.page.wait_for_url("**")