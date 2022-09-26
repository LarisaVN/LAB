#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#
import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")

# Базовый класс исключений для этого проекта
class APIException(Exception):
     pass


 #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "search-field")))

# 1 Оформление по кнопке с неполной надписью (Оформить)
@pytest.mark.nondestructive
def test_find_book():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(3)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    #time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    #time.sleep(10)

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    #time.sleep(3)

    #button_back_basket = drv.find_element_by_class_name("base-button--content")
    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()

    drv.quit()

    # Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'

# 2 Нет ни одной книги
@pytest.mark.nondestructive
def test_unfind_book():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("йцуукавыываа")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(10)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    srch_table[0].click()

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    #time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    #time.sleep(10)

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    #time.sleep(3)

    #button_back_basket = drv.find_element_by_class_name("base-button--content")
    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()

    drv.quit()

    #Если дошел до этого места
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'


# 3 Оформление по кнопке с полной надписью (Оформить заказ)
@pytest.mark.nondestructive
def test_find_book_fl_link_txt():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(10)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    srch_table[0].click()

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    #time.sleep(3)

    # Нажимаем кнопку "Оформить заказ"
    button_inbask = drv.find_element_by_link_text("Оформить заказ")
    button_inbask.click()
    #time.sleep(10)

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    #time.sleep(3)

    #button_back_basket = drv.find_element_by_class_name("base-button--content")
    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'


# 4 Размещение в "Отложенные"
@pytest.mark.nondestructive
def test_find_put_book():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Учим Python, делая крутые игры")
    time.sleep(3)

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-srch-icon.b-header-e-sprite-background")
    button_search.click()
    time.sleep(3)

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем кнопку "Отложить"
    button_basket = drv.find_element_by_class_name("icon-fave.track-tooltip.js-open-deferred-block")
    button_basket.click()
    time.sleep(3)

    # Просмотр отложенных товаров
    button_basket = drv.find_element_by_class_name("b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a")
    button_basket.click()
    time.sleep(10)


# 5 Плюс дополнительные экземпляры по скидке
@pytest.mark.nondestructive
def test_plus_discount_num_book():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(3)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    #time.sleep(3)


    # Покупка нескольких книг (кол-во определяет продавец) со скидкой
    #("Добавить в корзину")
    button_discount = drv.find_element_by_id("buyto-buyids")
    button_discount.click()


    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    #time.sleep(10)

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    #time.sleep(3)

    #button_back_basket = drv.find_element_by_class_name("base-button--content")
    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'

# 6 Изменение количества в корзине через поле ввода
# (не превышая max len)
@pytest.mark.nondestructive
def test_num_book_in_basket():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(5)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    time.sleep(4)

    # Устанавливаем количество
    field_amount_in_basket = drv.find_element_by_class_name("quantity")
    #field_amount_in_basket.click()
    field_amount_in_basket.clear()
    field_amount_in_basket.send_keys("4")
    time.sleep(7)

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    time.sleep(1)

    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()
    time.sleep(1)

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()
    time.sleep(1)

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'


# 7 Изменение количества в корзине через поле ввода
# (не превышая max len)
@pytest.mark.nondestructive
def test_neg_num_book_in_basket():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(7)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    time.sleep(4)

    # Устанавливаем количество
    field_amount_in_basket = drv.find_element_by_class_name("quantity")
    #field_amount_in_basket.click()
    field_amount_in_basket.clear()
    field_amount_in_basket.send_keys("-4")
    time.sleep(7)

    # true_val = field_amount_in_basket.get_property("text")
    # .get_attribute('value')

    amount_in_basket = drv.find_element_by_class_name("b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a")

    try:
        true_val = int(amount_in_basket.text)
    except:
        drv.quit()
        raise APIException('Ошибка преобразования в целое')

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    time.sleep(1)

    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()
    time.sleep(1)

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()
    time.sleep(1)

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'
    assert true_val < 0, 'Сайт проигнорировал знак минус при вводе количества'

# 8 Изменение количества в корзине через поле ввода (2)
# (не превышая max len)
@pytest.mark.nondestructive
def test_neg_num_book_in_basket():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(7)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    time.sleep(4)

    # Устанавливаем количество
    field_amount_in_basket = drv.find_element_by_class_name("quantity")
    #field_amount_in_basket.click()
    field_amount_in_basket.clear()
    field_amount_in_basket.send_keys("4")
    time.sleep(7)

    # true_val = field_amount_in_basket.get_property("text")
    # .get_attribute('value')

    amount_in_basket = drv.find_element_by_class_name("b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a")

    try:
        true_val = int(amount_in_basket.text)
    except:
        drv.quit()
        raise APIException('Ошибка преобразования в целое')

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    time.sleep(1)

    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()
    time.sleep(1)

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()
    time.sleep(1)

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'
    assert true_val == 4, 'Количество в корзине не соответствует введенному значению'

# 9 Изменение количества в корзине через поле "+"
# (не превышая max len)
@pytest.mark.nondestructive
def test_neg_num_book_in_basket_():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Python")

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-btn")
    button_search.click()
    time.sleep(5)

    srch_table = drv.find_elements_by_class_name("genres-carousel__item")

    # Вычисляем количество книг в списке
    str_num = len(srch_table)

    if (str_num == 0):
        drv.quit()
        raise APIException('Нет ни одной книги!')

    DummyFlag = False

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()

    #Выбираем первый элемент из списка обнаруженных
    #Здесь бы надо явную задержки, т.к. иногда кричит про то, что этот элемент ненажимаемый!
    time.sleep(7)
    srch_table[0].click()
    time.sleep(7)

    # Нажимаем кнопку "В корзину"
    button_basket = drv.find_element_by_class_name("btn.btn-small.btn-primary.btn-buy")
    button_basket.click()
    time.sleep(3)

    # Нажимаем кнопку "Оформить"
    button_inbask = drv.find_element_by_link_text("Оформить")
    button_inbask.click()
    time.sleep(6)

    # Устанавливаем количество
    button_plus = drv.find_element_by_class_name("btn.btn-increase.btn-increase-cart")
    #button_plus = drv.find_element_by_link_text("+")
    time.sleep(2)
    button_plus.click()
    time.sleep(7)

    amount_in_basket = drv.find_element_by_class_name("b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a")

    try:
        true_val = int(amount_in_basket.text)
    except:
        drv.quit()
        raise APIException('Ошибка преобразования в целое')

    # Нажимаем кнопку "Перейти к оформлению"
    button_buy = drv.find_element_by_class_name("btn.btn-primary.btn-large.fright.start-checkout-js")
    button_buy.click()
    time.sleep(1)

    button_back_basket = drv.find_element_by_class_name("text-s.book-shelf__back-to-cart-btn.v-color--blue-link.set-min-width")
    button_back_basket.click()
    time.sleep(1)

    # Нажимаем кнопку "Очистить корзину"
    button_clear_basket = drv.find_element_by_class_name("b-link-popup")
    button_clear_basket.click()
    time.sleep(1)

    drv.quit()

    #Если дошел до этого места (лажа)
    DummyFlag = True

    assert str_num > 0, 'Нет ни одной книги в результатах поиска'
    assert DummyFlag == True, 'Ошибки при работе с элементами управления'
    assert true_val == 2, 'Количество книг в корзине не соответствует заданному'


# 10 Перемещение из "Отложенные" в "Корзину"
@pytest.mark.nondestructive
def test_find_put_book_basket():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");
    # В поле поиcка вводим название книги, которую хотим найти
    field_search = drv.find_element_by_id("search-field")
    field_search.click()
    field_search.clear()
    field_search.send_keys("Учим Python, делая крутые игры")
    time.sleep(3)

    # Нажимаем на лупу
    button_search = drv.find_element_by_class_name("b-header-b-search-e-srch-icon.b-header-e-sprite-background")
    button_search.click()
    time.sleep(3)

    # Если есть хоть один элемент - сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем кнопку "Отложить"
    button_basket = drv.find_element_by_class_name("icon-fave.track-tooltip.js-open-deferred-block")
    button_basket.click()
    time.sleep(3)

    # Просмотр отложенных товаров
    #button_basket = drv.find_element_by_class_name("b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a")
    #button_basket.click()

    # Перенос в корзину
    button_basket = drv.find_element_by_class_name("btn.buy-link.btn-primary")
    button_basket.click()
    time.sleep(10)

# 11 Возврат на главную страницу из "Что почитать?
@pytest.mark.nondestructive
def test_read_return_main():

    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем на ссылку "Лабиринт" для возврата на главную страницу
    button_lab = drv.find_element_by_class_name("b-header-b-logo-e-logo")
    button_lab.click()
    time.sleep(5)

# 12 Поиск смешных книг
@pytest.mark.nondestructive
def test_find_book_funny():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Ха-Ха" (Смешная)
    button_funny = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-1.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_funny.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 13 Поиск грустных книг
@pytest.mark.nondestructive
def test_find_book_sad():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Глаз" (Грустная)
    button_sad = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-2.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_sad.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 14 Поиск вдохновляющих книг
@pytest.mark.nondestructive
def test_find_book_mood():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Змей" (Вдохновляющая)
    button_mood = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-3.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_mood.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 15 Поиск страшных книг
@pytest.mark.nondestructive
def test_find_book_terr():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Приведение" (Страшная)
    button_terr = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-4.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_terr.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 16 Поиск книг про любовь
@pytest.mark.nondestructive
def test_find_book_love():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Сердечко" (Про любовь)
    button_love = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-5.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_love.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 17 Поиск книг про расследования
@pytest.mark.nondestructive
def test_find_book_crim():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Вопрос" (Про расследования)
    button_crim = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-133.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_crim.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 18 Поиск книг про одиночество
@pytest.mark.nondestructive
def test_find_book_alone():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Единица" (Про одиночество)
    button_alone = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-6.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_alone.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 19 Поиск книг про кино
@pytest.mark.nondestructive
def test_find_book_movie():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Хлопушка" (Про кино)
    button_movie = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-7.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_movie.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 20 Поиск книг про здоровье
@pytest.mark.nondestructive
def test_find_book_health():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Аптечка" (Про здоровье)
    button_health = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-8.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_health.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 21 Поиск книг про семью
@pytest.mark.nondestructive
def test_find_book_family():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Дом" (Про семью)
    button_family = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-10.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_family.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 22 Поиск книг про невероятное
@pytest.mark.nondestructive
def test_find_book_unknown():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Гуманоид" (Про невероятное)
    button_unknown = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-11.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_unknown.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 23 Поиск книг про бизнес и успех
@pytest.mark.nondestructive
def test_find_book_luck():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Диаграммы" (Про бизнес и успех)
    button_luck = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-12.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_luck.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 24 Поиск книг про историю
@pytest.mark.nondestructive
def test_find_book_story():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Часы" (Про историю)
    button_story = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-13.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_story.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 25 Поиск книг про творчество
@pytest.mark.nondestructive
def test_find_book_creat():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Краски" (Про творчество)
    button_creat = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-24.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_creat.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 26 Поиск книг про духовный и личностный рост
@pytest.mark.nondestructive
def test_find_book_change():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Лестница" (Про духовный и личностный рост)
    button_change = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-25.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_change.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 27 Поиск познавательных книг
@pytest.mark.nondestructive
def test_find_book_explore():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Яблоко" (Познавательная)
    button_explore = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-17.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_explore.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 28 Поиск художественных книг
@pytest.mark.nondestructive
def test_find_book_fict():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Листик" (Художественная)
    button_fict = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-16.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_fict.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 29 Поиск поэзии
@pytest.mark.nondestructive
def test_find_book_poet():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Текст" (Поэзия)
    button_poet = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-116.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_poet.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 30 Поиск переведенных книг
@pytest.mark.nondestructive
def test_find_book_trans():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Страна" на ссылку "Глобус" (Переведенная)
    button_trans = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-14.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_trans.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 31 Поиск отечественных книг
@pytest.mark.nondestructive
def test_find_book_local():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Страна" на ссылку "Мордочка" (Отечественная)
    button_local = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-15.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_local.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 32 Поиск актуальных книг
@pytest.mark.nondestructive
def test_find_book_top():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Еще" на ссылку "Холм" (Актуальная)
    button_top = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-18.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_top.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 33 Поиск умных книг
@pytest.mark.nondestructive
def test_find_book_smart():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Еще" на ссылку "Бот" (Умная)
    button_smart = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-19.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_smart.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 34 Поиск подарочных книг
@pytest.mark.nondestructive
def test_find_book_gift():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Еще" на ссылку "Презент" (Подарочная)
    button_gift = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-20.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_gift.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 35 Поиск книг о премиях
@pytest.mark.nondestructive
def test_find_book_prem():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем в разделе "Еще" на ссылку "Медаль" (Премии)
    button_prem = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-134.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_prem.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 36 Переход на страницу "Детский навигатор"
@pytest.mark.nondestructive
def test_find_book_child():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)
    drv.quit()

# 37 Переход на страницу "Книжные обзоры"
@pytest.mark.nondestructive
def test_find_book_review():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Книжные обзоры"
    button_review = drv.find_element_by_link_text("Книжные обзоры")
    button_review.click()
    time.sleep(5)
    drv.quit()

# 38 Переход на страницу "Рецензии читателей"
@pytest.mark.nondestructive
def test_find_book_comment():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Рецензии читателей"
    button_comment = drv.find_element_by_link_text("Рецензии читателей")
    button_comment.click()
    time.sleep(5)
    drv.quit()


# 39 Переход на страницу "Подборки читателей"
@pytest.mark.nondestructive
def test_find_book_select():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Подборки читателей"
    button_select = drv.find_element_by_link_text("Подборки читателей")
    button_select.click()
    time.sleep(5)
    drv.quit()

# 40 Переход на страницу "Литтесты"
@pytest.mark.nondestructive
def test_find_book_littests():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Подборки читателей"
    button_littests = drv.find_element_by_link_text("Литтесты")
    button_littests.click()
    time.sleep(5)
    drv.quit()

# 41 Переход на страницу "Конкурсы"
@pytest.mark.nondestructive
def test_find_book_comp():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Конкурсы"
    button_comp = drv.find_element_by_link_text("Конкурсы")
    button_comp.click()
    time.sleep(5)
    drv.quit()

# 42 Поиск детских смешных книг
@pytest.mark.nondestructive
def test_find_book_child_funny():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Смешная"
    button_chfun = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-1.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chfun.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 43 Поиск детских серьезных книг
@pytest.mark.nondestructive
def test_find_book_child_ser():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Серьезная"
    button_chcer = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-27.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chcer.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 44 Поиск детских праздничных книг
@pytest.mark.nondestructive
def test_find_book_child_fest():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Настроение" на ссылку "Праздничная"
    button_fest = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-28.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_fest.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 45 Поиск детских сказок
@pytest.mark.nondestructive
def test_find_book_child_fairy():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Сказки"
    button_fairy = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-29.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_fairy.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 46 Поиск детских приключенческих книг
@pytest.mark.nondestructive
def test_find_book_child_advent():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Приключения"
    button_advent = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-30.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_advent.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 47 Поиск детских книг с картинками
@pytest.mark.nondestructive
def test_find_book_child_pict():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "С картинками"
    button_pict = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-31.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_pict.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 48 Поиск детских премиальных книг
@pytest.mark.nondestructive
def test_find_book_child_prem():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Премии"
    button_prem = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-135.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_prem.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 49 Поиск детских книг про детей
@pytest.mark.nondestructive
def test_find_book_child_about():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Про детей"
    button_about = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-32.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_about.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 50 Поиск детских книг про животных
@pytest.mark.nondestructive
def test_find_book_child_animal():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "О животных"
    button_animal = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-33.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_animal.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 51 Поиск детских книг про невероятное
@pytest.mark.nondestructive
def test_find_book_child_unknown():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "О чем" на ссылку "Про невероятное"
    button_unknown = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-34.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_unknown.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 52 Поиск книг для малышей
@pytest.mark.nondestructive
def test_find_book_child_small():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Возраст" на ссылку "Для малышей"
    button_chsm = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-35.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chsm.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 53 Поиск книг для детей
@pytest.mark.nondestructive
def test_find_book_child_medium():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Возраст" на ссылку "Для детей"
    button_chmed = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-21.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chmed.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 54 Поиск книг для подростков
@pytest.mark.nondestructive
def test_find_book_child_large():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Возраст" на ссылку "Для подростков"
    button_chlar = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-22.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chlar.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 55 Поиск книг для мальчиков
@pytest.mark.nondestructive
def test_find_book_child_boy():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Пол" на ссылку "Мальчик"
    button_boy = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-38.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_boy.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 56 Поиск книг для девочек
@pytest.mark.nondestructive
def test_find_book_child_girl():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Пол" на ссылку "Девочка"
    button_girl = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-39.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_girl.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 57 Поиск художественных книг для детей
@pytest.mark.nondestructive
def test_find_book_child_fict():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Художественная"
    button_chfic = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-42.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chfic.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 58 Поиск поэзии для детей
@pytest.mark.nondestructive
def test_find_book_child_poet():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Познавательная"
    button_chpoet = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-115.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chpoet.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 59 Поиск познавательных книг для детей
@pytest.mark.nondestructive
def test_find_book_child_explore():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Познавательная"
    button_chexp = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-41.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_chexp.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 60 Поиск детских книг про досуг
@pytest.mark.nondestructive
def test_find_book_child_time():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Жанр" на ссылку "Досуг"
    button_time = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-40.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_time.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 61 Поиск переведенных детских книг
@pytest.mark.nondestructive
def test_find_book_child_trans():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Страна" на ссылку "Переводная"
    button_trans = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-47.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_trans.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()

# 62 Поиск отечественных детских книг
@pytest.mark.nondestructive
def test_find_book_child_local():
    drv = webdriver.Chrome(executable_path="c:\ch_drv\chromedriver.exe", chrome_options=chrome_options)

    drv.implicitly_wait(30)

    # Заходим на сайт labirint.ru
    drv.get("https://www.labirint.ru//");

    # Сначала согласимся на куки
    button_cookie_accept = drv.find_element_by_class_name("cookie-policy__button.js-cookie-policy-agree")
    button_cookie_accept.click()
    time.sleep(3)

    # Нажимаем на ссылке "Что почитать? Рекомендуем"
    button_read = drv.find_element_by_class_name("b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long")
    button_read.click()
    time.sleep(5)

    # Нажимаем во вкладке "Что читать? Рекомендуем" на ссылку "Детский навигатор"
    button_child = drv.find_element_by_link_text("Детский навигатор")
    button_child.click()
    time.sleep(5)

    # Нажимаем в разделе "Страна" на ссылку "Наша"
    button_local = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-tag-48.b-goodssets-tags-e-tag-m-hovered.analytics-click-js")
    button_local.click()
    time.sleep(5)

    try:
         WebDriverWait(drv, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")))
    except:
         drv.quit()
         raise APIException('Не срабатывает клик на иконке группы книг')

    button_x = drv.find_element_by_class_name("pushstate.b-goodssets-tags-e-tag.b-goodssets-tags-e-reset.b-goodssets-tags-e-tag-m-hovered")
    button_x.click()
    drv.quit()




