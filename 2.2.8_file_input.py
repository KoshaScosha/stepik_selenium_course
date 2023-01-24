from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome()


try:
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Rick")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Sanchez")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("universe@sucks.com")
    file_button = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '2.2.8_file.txt') # добавляем к этому пути имя файла
    file_button.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
