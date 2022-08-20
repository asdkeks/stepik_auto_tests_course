import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = int(browser.find_element(By.ID, "input_value").text)
    number = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(number)

    check_input = browser.find_element(By.ID, "robotCheckbox")
    check_input.click()
    radio_input = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_input)
    radio_input.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()