from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

class TestRegistration(unittest.TestCase):


    def test_form1(self):
        browser.get("http://suninjuly.github.io/registration1.html")
        name_input = browser.find_element(By.CLASS_NAME, 'form-control.first:required')
        name_input.send_keys('Daemon')
        surname_input = browser.find_element(By.CLASS_NAME, 'form-control.second:required')
        surname_input.send_keys('Targaryen')
        email_input = browser.find_element(By.CLASS_NAME, 'form-control.third:required')
        email_input.send_keys('dragons_rule@fire.com')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(2)
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Wrong welcome text')
        time.sleep(10)
        browser.quit()

    def test_form2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        name_input = browser.find_element(By.CLASS_NAME, 'form-control.first:required')
        name_input.send_keys('Daemon')
        surname_input = browser.find_element(By.CLASS_NAME, 'form-control.second:required')
        surname_input.send_keys('Targaryen')
        email_input = browser.find_element(By.CLASS_NAME, 'form-control.third:required')
        email_input.send_keys('dragons_rule@fire.com')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(2)
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Wrong welcome text')
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()