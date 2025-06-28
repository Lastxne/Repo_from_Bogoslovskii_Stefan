import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation_safari():
    try:
        driver = webdriver.Safari()
    except Exception:
        pytest.skip("Safari недоступен или не включена автоматизация")

    driver.set_window_size(1280, 800)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_id, value in data.items():
            field = wait.until(
                EC.presence_of_element_located((By.NAME, field_id))
            )
            field.send_keys(value)

        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()

        # Ждём, пока zip получит класс
        wait.until(
            lambda d: "alert-danger"
            in d.find_element(By.ID, "zip-code").get_attribute("class")
        )
        zip_result = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_result.get_attribute("class")

        for field_id in data.keys():
            wait.until(
                lambda d: "alert-success"
                in d.find_element(By.ID, field_id).get_attribute("class")
            )
            field_result = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_result.get_attribute("class")

    finally:
        driver.quit()
