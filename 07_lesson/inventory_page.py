from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        button = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/following::button[1]"
        )
        button.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
