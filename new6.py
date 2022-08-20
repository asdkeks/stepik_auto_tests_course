import time
import os
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    x_text = browser.find_element(By.ID, "input_value").text
    x_math = str(math.log(abs(12 * math.sin(int(x_text)))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(x_math)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
