import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

def (browser):
    browser.get("https://basarab.prestaging.kokoc.tech/catalog/zhenskaya_obuv/botinki_na_kabluke/botilony_fieria_kozhanye_na_bayke/")
    elemet = browser.find_element()