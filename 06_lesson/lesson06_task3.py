from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    def img_has_src(d):
        el = d.find_element(By.ID, "award")
        return el if el.get_attribute("src") else False

    award_img = WebDriverWait(driver, 15).until(img_has_src)

    print(award_img.get_attribute("src"))

finally:
    driver.quit()
