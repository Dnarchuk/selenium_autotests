import pytest

from api import create_driver
from pages.start import StartPage


@pytest.fixture(scope='session')
def driver():
    webdriver = create_driver()
    yield webdriver
    webdriver.quit()


@pytest.fixture(scope='session')
def start_page(driver):
    page = StartPage(driver)
    page.go_to()
    yield page
    

@pytest.fixture(scope='function')
def search_book(start_page):
    start_page: StartPage
    start_page.search_entry_field
    start_page.open()
    start_page.search_entry_field
    return start_page