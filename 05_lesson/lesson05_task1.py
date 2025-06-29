from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    time.sleep(2)

finally:
    driver.quit()
