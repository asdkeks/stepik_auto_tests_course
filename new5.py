import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'new5.txt')

    first_name_input = browser.find_element(By.NAME, "firstname")
    first_name_input.send_keys("Test")
    last_name_input = browser.find_element(By.NAME, "lastname")
    last_name_input.send_keys("Test")
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("Test")

    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
