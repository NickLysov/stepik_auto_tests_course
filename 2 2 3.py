from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import math
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input1.send_keys('1')
    input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
    input2.send_keys('1')
    input3 = browser.find_element(By.XPATH, "//input[@name='email']")
    input3.send_keys('1')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.XPATH, "//input[@type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()