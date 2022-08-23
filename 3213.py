import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEl(unittest.TestCase):
    def TestEl1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        first_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
        first_name_input.send_keys("Test")
        last_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
        last_name_input.send_keys("Test")
        email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
        email_input.send_keys("Test")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Something went wrong!")

    def TestEl2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        first_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
        first_name_input.send_keys("Test")
        last_name_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
        last_name_input.send_keys("Test")
        email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
        email_input.send_keys("Test")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Something went wrong!")


if __name__ == "__main__":
    unittest.main()
