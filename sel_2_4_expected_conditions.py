import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(driver, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))

button_book = driver.find_element_by_css_selector("button.btn.btn-primary")
button_book.click()

x = int(driver.find_element_by_css_selector("#input_value").text)

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

answer = calc(x)

answer_input = driver.find_element_by_css_selector("#answer")
answer_input.send_keys(answer)

answer_submit = driver.find_element_by_css_selector("body > form > div > div > button")
answer_submit.click()

time.sleep(5)

driver.quit()

