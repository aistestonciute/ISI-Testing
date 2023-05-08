import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistrationForm(unittest.TestCase):
    def __init__(self, methodName, url):
        super().__init__(methodName)
        self.url = url

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver

        driver.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Vardenis")
        driver.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Pavardenis")
        driver.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("vardenis.pavardenis@pastas.lt")

        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        #laukia 5 s
        driver.implicitly_wait(5)

if __name__ == "__main__":
    urls = [
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
    ]

    runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    
    for url in urls:
        test_suite.addTest(TestRegistrationForm('test_registration', url))
    
    runner.run(test_suite)
