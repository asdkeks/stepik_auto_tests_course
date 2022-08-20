import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    number = str(num1 + num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(number)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()