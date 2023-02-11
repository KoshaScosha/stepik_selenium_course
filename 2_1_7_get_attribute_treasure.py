from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element(By.TAG_NAME, 'img')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    answer_element.send_keys(y)
    rob_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    rob_checkbox.click()
    rob_radio = browser.find_element(By.ID, 'robotsRule')
    rob_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()