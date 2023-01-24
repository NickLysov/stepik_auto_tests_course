from selenium.webdriver.common.by import By
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items_find_button(browser):
    browser.get(link)
    #time.sleep(5)
    y = len(browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert y > 0, 'Требуемый селектор не был найден.'   
