import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "http://suninjuly.github.io/explicit_wait2.html"
driver.get(url)

#laukimas iki kol price bus 100
wait = WebDriverWait(driver, 12)
price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

#book mygtuko paspaudimas
book_button = driver.find_element(By.ID, "book")
book_button.click()

#formules sprendimas
print('Solving')
input_value_element = driver.find_element(By.ID, 'input_value')
input_value = input_value_element.text
result = math.log(abs(12 * math.sin(int(input_value))))

driver.quit()
