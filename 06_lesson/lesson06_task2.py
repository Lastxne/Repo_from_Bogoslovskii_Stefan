from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    WebDriverWait(driver, 5).until(lambda d: button.text == "SkyPro")
    print(button.text)

finally:
    driver.quit()
