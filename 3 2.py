from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("zd@ro.va")
        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys("8-800-555-35-35")
        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys("baza")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("zd@ro.va")
        input4 = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        input4.send_keys("8-800-555-35-35")
        input5 = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        input5.send_keys("baza")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)	
        
if __name__ == "__main__": unittest.main()