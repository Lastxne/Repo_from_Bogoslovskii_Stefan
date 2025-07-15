from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    success_block = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    WebDriverWait(driver, 5).until(
        lambda d: "Data loaded with AJAX get request." in success_block.text
    )

    print(success_block.text.strip())

finally:
    driver.quit()
