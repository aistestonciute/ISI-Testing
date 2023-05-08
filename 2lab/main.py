from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/simple_form_find_task.html")

first_name_field = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
print("First name field:", first_name_field)
first_name_field.send_keys("Aiste")

last_name_field = browser.find_element(By.CSS_SELECTOR, "input[name='last_name']")
print("Last name field:", last_name_field)
last_name_field.send_keys("Stonciute")

city_field = browser.find_element(By.CLASS_NAME, "city")
print("City field::", city_field)
city_field.send_keys("Siauliai")

country_field = browser.find_element(By.ID, "country")
print("Country field:", country_field)
country_field.send_keys("Lithuania")

submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Submit button:", submit_button)
submit_button.click()

browser.quit()

print("Success!")
