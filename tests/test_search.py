import time

from pages.start import StartPage
from selenium.webdriver.common.keys import Keys

# Тесты через PageObject
#Case 5  
# переход в раздел доставки с главной страницы
def test_delivery(start_page):
    start_page: StartPage
    start_page.scroll_to_end_page_main()
    time.sleep(2)
    start_page.search_delivery
    start_page.delivery_button_click()
    page = start_page.search_title_delivery()
    assert "Виды доставки" in page[0].text

# #Case 6
# поиск блокнот на сайте через поиск
def test_page_after_search(search_book):
    search_book.search_name_input('Блокнот')
    search_book.search_name_input(Keys.RETURN)
    page = search_book.text_notepad_in_search()
    assert 'Блокнот' in page.text or 'блокнот' in page.text

# Case 7
# сортировка по алфавиту на странице с найденными блокнотами
def test_by_alphabet(search_book):
    search_book.search_name_input('Блокнот')
    search_book.search_name_input(Keys.RETURN)
    search_book.button_relevants()
    search_book.button_relevants_click()
    search_book.button_alphabet()
    search_book.button_alphabet_click()

#Case 8 Переход на страницу персональных данных и открытие оформления заказа
def test_personal_data(start_page):
    start_page: StartPage
    start_page.scroll_to_end_page_main()
    start_page.search_title_personal_data
    start_page.personal_data_button_click()
    page = start_page.search_title_personal_data()
    assert "Обработка персональных данных" in page[0].text


# Case 9 Проверка открытия раздела "О компании"
def test_company_page(start_page):
    start_page: StartPage
    start_page.scroll_to_end_page_main()
    start_page.search_title_personal_data
    start_page.personal_data_button_click()
    start_page.button_about_company
    start_page.button_about_company_click()
    title = start_page.search_title_about_company
    assert "О компании" in title[0]