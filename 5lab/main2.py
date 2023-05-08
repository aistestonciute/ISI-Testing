import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function", params=[
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html"
], ids=["registration1", "registration2"])
def registration_form_url(request):
    yield request.param

@pytest.mark.usefixtures("driver")
class TestRegistrationForm:
    @pytest.mark.parametrize("name, last_name, email", [("Vardenis", "Pavardenis", "vardenis.pavardenis@pastas.lt")])
    def test_registration(self, driver, registration_form_url, name, last_name, email):
        driver.get(registration_form_url)

        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys(name)
        driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys(last_name)
        driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(email)

        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        driver.implicitly_wait(5)
