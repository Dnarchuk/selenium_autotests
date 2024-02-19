from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service, options=options)
    driver.implicitly_wait(0.5)
    return driver