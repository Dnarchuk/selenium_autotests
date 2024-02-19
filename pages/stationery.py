from pages.base import BasePage
from selenium.webdriver.common.by import By
from config.const import BASE_URL, NOTEPAD_URL


class NotepadPage(BasePage):  
    URL = f'{BASE_URL}/'
    
    def __init__(self, driver, url: str):
        super().__init__(driver)
        self.URL = url

    def open_notepad_page(self):
        self.driver.get(NOTEPAD_URL)