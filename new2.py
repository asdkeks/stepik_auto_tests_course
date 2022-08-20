import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_text = browser.find_element(By.ID, "treasure")
    x = int(x_text.get_attribute("valuex"))
    x_math = str(math.log(abs(12*math.sin(int(x)))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x_math)
    check_input = browser.find_element(By.ID, "robotCheckbox")
    check_input.click()
    radio_input = browser.find_element(By.ID, "robotsRule")
    radio_input.click()


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
