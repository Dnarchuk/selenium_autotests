import time

from config.const import FULL_PATH
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.notepad import NotepadPage

from config.const import BASE_URL

# Case 1
# Открытие страницы товара с описанием
def test_open_page_item(driver):
    driver.get(BASE_URL)
    search_button = driver.find_element(By.XPATH, '//input[@placeholder="Введите название товара"]')
    search_button.send_keys('Блокнот')
    search_button.send_keys(Keys.RETURN)
    search_button_relevants = driver.find_element(By.XPATH, '//span[text() = "По релевантности"]')
    search_button_relevants.click()
    search_button_by_alphabetically = driver.find_element(By.XPATH, '//a[@data-sort="abc_asc"]')
    search_button_by_alphabetically.click()
    assert driver.current_url.endswith("abc_asc")
    time.sleep(2)
    search_notebook = driver.find_element(By.XPATH, '//div[@data-value="10468733"]')
    search_notebook.click()
    search_title = driver.find_elements(By.XPATH, '//div[@class="b-product-title__heading"]')
    assert search_title
    assert "75 головоломок. Умный блокнот" in search_title[0].text
    driver.save_screenshot(f'{FULL_PATH}/page_with_notebook.png')


# Case 2
# переход на страницу канцелярские товары со страницы с блокнотами
def test_search_stationery(driver):
    driver.get(BASE_URL)
    search_button = driver.find_element(By.XPATH, '//input[@placeholder="Введите название товара"]')
    search_button.send_keys('Блокнот')
    search_button.send_keys(Keys.RETURN)
    time.sleep(2)
    search_stationery = driver.find_element(By.XPATH, '//span[text() = "Канцтовары, учёба"]')
    search_stationery.click()


# Case 3
# сортировка по бренду oz в разделе концелярские товары
def test_sorting_by_brand_oz(driver):
    driver.get(BASE_URL)
    search_button = driver.find_element(By.XPATH, '//input[@placeholder="Введите название товара"]')
    search_button.send_keys('Блокнот')
    search_button.send_keys(Keys.RETURN)
    time.sleep(2)
    search_stationery = driver.find_element(By.XPATH, '//span[text() = "Канцтовары, учёба"]')
    search_stationery.click()
    search_checkbox_oz = driver.find_element(By.XPATH, '//label[@for="id_producer_1201511"]')
    search_checkbox_oz.click()
    driver.find_element(By.XPATH, '//span[@class="dp-base dp-showresults dp-showresults_exist"]')
    search_shown_items = driver.find_element(By.XPATH, '//span[@class="dp-showresults__content"]')
    search_shown_items.click()
    expected_url = driver.current_url
    assert expected_url == "https://oz.by/search/?availability=1;2;3&c=1113115&id_producer=1201511&q=%D0%91%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82&sort=relev_desc&type=10"
    driver.save_screenshot(f'{FULL_PATH}/sorting_by_oz.png')


#Case 4 фильтр по распродаже на странице с блокнотами
def test_filtering_sales(driver):
    driver.get(BASE_URL)
    search_button = driver.find_element(By.XPATH, '//input[@placeholder="Введите название товара"]')
    search_button.send_keys('Блокнот')
    search_button.send_keys(Keys.RETURN)
    search_button_sales = driver.find_element(By.XPATH, '//label[@for="sl_1"]')
    search_button_sales.click()
    expected_url = driver.current_url
    assert expected_url == "https://oz.by/search/?availability=1;2;3&c=0&q=%D0%91%D0%BB%D0%BE%D0%BA%D0%BD%D0%BE%D1%82&sl=1&sort=best_desc&type=0"


  