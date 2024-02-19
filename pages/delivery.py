from pages.base import BasePage
from selenium.webdriver.common.by import By
from config.const import BASE_URL, DELIVERY_URL


class Locators:
    TITLE_DELIVERY = (By.XPATH, '//h1[text()="Виды доставки"]')



class DeliveryPage(BasePage): 
    URL = f'{BASE_URL}/'

    def __init__(self, driver, url: str):
        super().__init__(driver)
        self.URL = url

    def open_delivery_page(self):
        self.driver.get(DELIVERY_URL)