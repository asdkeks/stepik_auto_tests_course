from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    number = str(math.log(abs(12 * math.sin(int(x)))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(number)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
