import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Раскомментируйте следующую строку для визуальной проверки языка
    # time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR,"button.btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Add to basket button is not found"
