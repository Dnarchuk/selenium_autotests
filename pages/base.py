from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_DEFAULT_TIMEOUT = 15

class BasePage:
    URL = None
    
    def __init__(self, driver: Chrome):
        self.driver = driver
        self._waiting = WebDriverWait(self.driver, _DEFAULT_TIMEOUT)

    
    def find(self, locator: tuple[str, str]) -> WebElement:
        return self._waiting.until(EC.presence_of_element_located(locator))
    

    def finds(self, locator: tuple[str, str]) -> WebElement:
        return self._waiting.until(EC.presence_of_all_elements_located(locator))
    

    def click_to(self, locator: tuple[str, str]):
        element = self.find(locator)
        element.click()
        return element
    
    def go_to(self):
        self.driver.get(self.URL)
        self._waiting.until(EC.url_to_be(self.URL))

    def check_current_url(self):
        url = self.current_url
        return url(self.driver, url)