from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализация страницы логина.

        :param driver: Объект WebDriver для работы с браузером (тип: WebDriver)
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """
        Открывает страницу логина.

        :return: None
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными учетными данными.

        :param username: Имя пользователя (тип: str)
        :param password: Пароль (тип: str)
        :return: None
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
