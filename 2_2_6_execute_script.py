from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.set_window_size(1280, 720)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    answer_element.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    rob_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    rob_checkbox.click()
    rob_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    rob_radio.click()
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
