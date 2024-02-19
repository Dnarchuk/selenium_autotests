from pages.base import BasePage
from selenium.webdriver.common.by import By
from config.const import BASE_URL



class Locators:
    BUTTON_RELEVANTS = (By.XPATH, '//span[text() = "По релевантности"]')
    BUTTON_ALPHABET = (By.XPATH, '//a[@data-sort="abc_asc"]')


class NotepadPage(BasePage):  
    URL = f'{BASE_URL}/'
    
    def __init__(self, driver, url: str):
        super().__init__(driver)
        self.URL = url
    
    def button_relevants(self) -> str:
        return self.find(Locators.BUTTON_RELEVANTS)
    
    def button_relevants_click(self):
        return self.click_to(Locators.BUTTON_RELEVANTS)
    
    def button_alphabet(self) -> str:
        return self.find(Locators.BUTTON_ALPHABET)
    
    def button_alphabet_click(self):
        return self.click_to(Locators.BUTTON_ALPHABET)