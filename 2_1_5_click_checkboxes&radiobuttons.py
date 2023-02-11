from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    answer_element.send_keys(y)
    rob_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    rob_checkbox.click()
    rob_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    rob_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
