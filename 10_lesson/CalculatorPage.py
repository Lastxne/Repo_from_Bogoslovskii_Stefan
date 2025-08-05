from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: Объект WebDriver для работы с браузером. Тип: WebDriver.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку перед выполнением вычислений.

        :param seconds: Задержка в секундах. Тип: int.
        :return: None
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, value: str) -> None:
        """
        Нажимает на кнопку калькулятора с указанным значением.

        :param value: Значение кнопки. Тип: str.
        :return: None
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        )
        button.click()

    def get_result(
        self, expected_value: str = "15", timeout: int = 55
    ) -> bool:
        """
        Получает результат вычисления с экрана калькулятора и проверяет его.

        :param expected_value: Ожидаемое значение на экране. Тип: str.
        :param timeout: Время ожидания до получения результата. Тип: int.
        :return: True, если результат соответствует ожиданиям, иначе False.
            Тип: bool.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected_value
            )
        )
