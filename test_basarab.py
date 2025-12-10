import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()




def test_fast_buy(browser):
    browser.get("https://basarab.prestaging.kokoc.tech/catalog/zhenskaya_obuv/botinki_na_kabluke/botilony_fieria_kozhanye_na_bayke/")
    buton_size = browser.find_element(By.XPATH,"//input[@data-razmer='38']")
    buton_size.click()
    button_add_basket = browser.find_element(By.XPATH,"//button[@class='btn btn-gradient btn--stroke btn--big js-fast-oder']")
    button_add_basket.click()
    time.sleep(3)
    #телефон
    input_phone = browser.find_elements(By.XPATH, "//input[@id='fastFormProductPhone']")
    input_phone[0].click()  # для работы с маской, сначала надо нажать на поле
    input_phone[0].send_keys("9879993863")
    #имя
    input_name = browser.find_element(By.XPATH,"//input[@id='fastFormName']")
    input_name.send_keys("тест")
    #фамилия
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormSurName']")
    input_name.send_keys("тест")
    #Отчество
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormPatronymic']")
    input_name.send_keys("тест")
    #почта
    input_name = browser.find_element(By.XPATH, "//input[@id='fastFormEmail']")
    input_name.send_keys("test@test.test")
    #текст
    input_name = browser.find_element(By.XPATH, "//textarea[@id='fastFormComment']")
    input_name.send_keys("тест")
    #оформление заказа
    input_name = browser.find_element(By.XPATH, "//button[@class='btn btn-black btn--stroke btn--big js-fast-form-send-button fast-order-tovar']")
    input_name.click()
    time.sleep(3)

