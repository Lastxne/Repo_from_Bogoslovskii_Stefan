from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        """
        Инициализация страницы инвентаря.

        :param driver: Объект WebDriver для работы с браузером (тип: WebDriver)
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину.

        :param product_name: Название товара (тип: str)
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/following::button[1]"
        )
        button.click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
