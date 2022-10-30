from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
output_element = 0

try:
    browser.get("http://suninjuly.github.io/registration1.html")
    required_input_list = browser.find_elements(By.XPATH, '//input[@required]')
    output_list = ['Daemon', 'Targaryen', 'dragons_rule@fire.com']

    for input in required_input_list:
        input.send_keys(output_list[output_element])
        output_element += 1

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
