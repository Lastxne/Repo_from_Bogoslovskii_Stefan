from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: Объект WebDriver для работы с браузером (тип: WebDriver)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
        self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """
        Заполняет форму с данными покупателя и продолжает процесс оформления.

        :param first_name: Имя покупателя (тип: str)
        :param last_name: Фамилия покупателя (тип: str)
        :param zip_code: Почтовый индекс (тип: str)
        :return: None
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        ).send_keys(first_name)

        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получает общую сумму заказа.

        :return: Сумма заказа (тип: str)
        """
        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text.strip()
