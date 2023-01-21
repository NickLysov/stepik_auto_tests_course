from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = int((browser.find_element(By.XPATH, "//span[@id='num1']")).text)
    y_element = int((browser.find_element(By.XPATH, "//span[@id='num2']")).text)
    sum = str(x_element+y_element)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()