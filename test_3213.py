import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEl(unittest.TestCase):
    def TestEl1(self):
        browser1 = webdriver.Chrome()
        browser1.get("http://suninjuly.github.io/registration1.html")
        first_name_input1 = browser1.find_element(By.CSS_SELECTOR, "div.first_block .first")
        first_name_input1.send_keys("Test")
        last_name_input1 = browser1.find_element(By.CSS_SELECTOR, "div.first_block .second")
        last_name_input1.send_keys("Test")
        email_input1 = browser1.find_element(By.CSS_SELECTOR, "div.first_block .third")
        email_input1.send_keys("Test")
        button1 = browser1.find_element(By.CSS_SELECTOR, "button.btn")
        button1.click()
        time.sleep(1)
        welcome_text_elt1 = browser1.find_element(By.TAG_NAME, "h1")
        welcome_text1 = welcome_text_elt1.text
        self.assertEqual(welcome_text1, "Congratulations! You have successfully registered!", "Something went wrong!")
        pass

    def TestEl2(self):
        browser2 = webdriver.Chrome()
        browser2.get("http://suninjuly.github.io/registration2.html")
        first_name_input2 = browser2.find_element(By.CSS_SELECTOR, "div.first_block .first")
        first_name_input2.send_keys("Test")
        last_name_input2 = browser2.find_element(By.CSS_SELECTOR, "div.first_block .second")
        last_name_input2.send_keys("Test")
        email_input2 = browser2.find_element(By.CSS_SELECTOR, "div.first_block .third")
        email_input2.send_keys("Test")
        button2 = browser2.find_element(By.CSS_SELECTOR, "button.btn")
        button2.click()
        time.sleep(1)
        welcome_text_elt2 = browser2.find_element(By.TAG_NAME, "h1")
        welcome_text2 = welcome_text_elt2.text
        self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!", "Something went wrong!")
        pass


if __name__ == "__main__":
    unittest.main()
