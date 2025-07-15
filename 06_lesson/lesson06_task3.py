from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
)

img = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "award"))
)
print(img.get_attribute("src"))

driver.quit()
