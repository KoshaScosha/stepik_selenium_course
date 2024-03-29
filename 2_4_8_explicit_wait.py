from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    book_button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    book_button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    answer_element.send_keys(y)
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()