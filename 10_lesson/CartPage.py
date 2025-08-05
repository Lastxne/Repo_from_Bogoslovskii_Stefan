from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: Объект WebDriver для работы с браузером (тип: WebDriver)
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """
        Нажимает кнопку "Checkout" для перехода к оформлению заказа.

        :return: None
        """
        self.driver.find_element(By.ID, "checkout").click()
