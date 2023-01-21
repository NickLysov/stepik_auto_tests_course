from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int((browser.find_element(By.XPATH, "//span[@id='input_value']")).text)
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    input2 = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    input2.click()
    input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()