import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class", params=[
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html"
])
def registration_form_url(request):
    yield request.param

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestRegistrationForm:
    def test_registration(self, driver, registration_form_url):
        driver.get(registration_form_url)

        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Vardenis")
        driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Pavardenis")
        driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("vardenis.pavardenis@pastas.lt")

        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        driver.implicitly_wait(5)
