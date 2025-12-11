from asyncio import wait

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

def search_input(browser, s):
    # телефон
    input_phone = browser.find_elements(By.XPATH, "//input[@id='fastFormProductPhone']")
    input_phone[s].click()  # для работы с маской, сначала надо нажать на поле
    input_phone[s].send_keys("9879993863")
    # имя
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormName']")
    input_name.send_keys("тест")
    # фамилия
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormSurName']")
    input_name.send_keys("тест")
    # Отчество
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormPatronymic']")
    input_name.send_keys("тест")
    # почта
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormEmail']")
    input_name.send_keys("test@test.test")
    # текст
    input_name = browser.find_element(By.XPATH, "//textarea[@id='fastFormComment']")
    input_name.send_keys("тест")

def create_order(browser):
    input_name = browser.find_element(By.XPATH,"//button[@class='btn btn-black btn--stroke btn--big js-fast-form-send-button fast-order-tovar']")
    input_name.click()

def fast_basket(browser):
    button_add_basket = browser.find_element(By.XPATH, "//button[@class='btn btn-black btn--stroke btn--big js-product-additions-open js-sticky-buttons-trigger js-add-basket']")
    button_add_basket.click()
    button_open_basket = browser.find_element(By.XPATH, "//a[@data-type='basket']")
    button_open_basket.click()

    wai = WebDriverWait(browser, 10)

    button_fast = wai.until(
        EC.presence_of_element_located(By.XPATH, "//button[@class='btn btn-black border btn--stroke btn--medium fast-order-btn']")
        ) #пофиксить корзину
    button_fast.click()
    search_input(browser, 1)
    time.sleep(3)




def fast_buy(browser):

    button_add_basket = browser.find_element(By.XPATH,"//button[@class='btn btn-gradient btn--stroke btn--big js-fast-oder']")
    button_add_basket.click()
    time.sleep(3)
    search_input(browser,0)
    # time.sleep(3)

def test_fast_orders(browser):
    browser.get("https://basarab.prestaging.kokoc.tech/catalog/zhenskaya_obuv/botinki_na_kabluke/botilony_fieria_kozhanye_na_bayke/")
    buton_size = browser.find_element(By.XPATH, "//input[@data-razmer='37']")
    buton_size.click()
    fast_buy(browser)
    browser.switch_to.active_element.send_keys(Keys.ESCAPE)
    time.sleep(2)
    buton_size = browser.find_element(By.XPATH, "//input[@data-razmer='39']")
    buton_size.click()
    fast_basket(browser)
    browser.switch_to.active_element.send_keys(Keys.ESCAPE)
    time.sleep(3)