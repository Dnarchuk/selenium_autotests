from pages.base import BasePage
from pages.notepad import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config.const import BASE_URL

_DEFAULT_TIMEOUT = 15


class Locators:
    BUTTON_SELECTOR = (By.XPATH, '//input[@placeholder="Введите название товара"]')
    BUTTON_DELIVERY = (By.XPATH, '//a[@href="/help/assistant.phtml?l=i.order.supply"]')
    FIND_TEXT = (By.XPATH, ' //span[@class="breadcrumbs__list__item"]')
    HTML = (By.TAG_NAME, 'html')
    TITLE_DELIVERY = (By.XPATH, '//h1[text()="Виды доставки"]')
    BUTTON_RELEVANTS = (By.XPATH, '//span[text() = "По релевантности"]')
    BUTTON_ALPHABET = (By.XPATH, '//a[@data-sort="abc_asc"]')
    BUTTON_PERSONAL_DATA = (By.XPATH,'//a[@href="/help/privacy.policy"]')
    TITLE_PERSONAL_DATA = (By.XPATH, '//div[@class="faq__title"]')
    SORTING_ALPHABET = (By.XPATH, '//span[@class="top-filters__eselect__item top-filters__viewer__open"]')
    ABOUT_COMPANY = (By.XPATH, '//a[@href="/help/about.us"]')
    TITLE_ABOUT_COMPANY = (By.XPATH, '//div[text()="О компании"]')



class StartPage(BasePage):
    URL = f'{BASE_URL}/'
    
    def __init__(self, driver):
        self.driver = driver
        self._waiting = WebDriverWait(self.driver, _DEFAULT_TIMEOUT)

    def open(self):
        self.driver.get(BASE_URL)
    
    def search_entry_field(self):
        return self.find(Locators.BUTTON_SELECTOR)
    
    def search_name_input(self, request_string: str):
        search_field = self.find(Locators.BUTTON_SELECTOR)
        search_field.send_keys(request_string)

    def scroll_to_end_page_main(self):
        html = self.find(Locators.HTML)
        html.send_keys(Keys.END)

    def search_delivery(self) -> list[str]:
        return self.finds(Locators.BUTTON_DELIVERY)

    def delivery_button_click(self):
        return self.click_to(Locators.BUTTON_DELIVERY)
    
    def text_notepad_in_search(self):
        return self.find(Locators.FIND_TEXT)
    
    def search_title_delivery(self):
        return self.finds(Locators.TITLE_DELIVERY)
    
    def search_button_personal_data(self):
        return self.finds(Locators.BUTTON_PERSONAL_DATA)
    
    def personal_data_button_click(self):
        return self.click_to(Locators.BUTTON_PERSONAL_DATA)
    
    def search_title_personal_data(self):
        return self.finds(Locators.TITLE_PERSONAL_DATA)

    def button_relevants(self) -> str:
        return self.find(Locators.BUTTON_RELEVANTS)
    
    def button_relevants_click(self):
        return self.click_to(Locators.BUTTON_RELEVANTS)
    
    def button_alphabet(self) -> str:
        return self.find(Locators.BUTTON_ALPHABET)
    
    def button_alphabet_click(self):
        return self.click_to(Locators.BUTTON_ALPHABET)

    def sorting_by_alphabet(self):
        return self.find(Locators.SORTING_ALPHABET)
    
    def button_about_company(self) -> str:
        return self.find(Locators.ABOUT_COMPANY)
    
    def button_about_company_click(self) -> str:
        return self.click_to(Locators.ABOUT_COMPANY)
    
    def search_title_about_company(self):
        return self.find(Locators.TITLE_ABOUT_COMPANY)
