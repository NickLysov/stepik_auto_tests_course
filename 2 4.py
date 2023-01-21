from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    x = int((browser.find_element(By.XPATH, "//span[@id='input_value']")).text)
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[@id='solve']")
    button.click()
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])   # сохранить в буфер
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()