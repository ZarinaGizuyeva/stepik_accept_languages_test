import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_presence(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    button_text = add_to_basket_button.text
    assert add_to_basket_button.text == button_text, 'add to basket button is not displayed'