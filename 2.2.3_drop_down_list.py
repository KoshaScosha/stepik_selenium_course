from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    browser.get('https://suninjuly.github.io/selects1.html')
    first_number_element = browser.find_element(By.ID, 'num1')
    second_number_element = browser.find_element(By.ID, 'num2')
    first_number = first_number_element.text
    second_number = second_number_element.text
    sum = str(int(first_number) + int(second_number))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()