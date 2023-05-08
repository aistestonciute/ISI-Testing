from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def solve():
    driver.get('http://suninjuly.github.io/alert_accept.html')

    #Mygtuko paspaudimas
    print('Button click')
    button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    #ant alert paspaudi
    print('Accept alert')
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    #formules sprendimas 
    print('Solving the task')
    input_value_element = driver.find_element(By.ID, 'input_value')
    input_value = input_value_element.text
    result = math.log(abs(12 * math.sin(int(input_value))))

    #atsakymo irasymas i lauka
    print('Enter answer')
    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.send_keys(str(result))


    #submit
    print('Submit')
    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

def main_functions():
    driver.get('http://suninjuly.github.io/redirect_accept.html')

    #redirectina pasaudus mygtuka submit
    button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    #naujas tab nuejimas
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])

    #perskaito formule ir apskaiciuoja rezultata
    input_value_element = driver.find_element(By.ID, 'input_value')
    input_value = input_value_element.text
    result = math.log(abs(12 * math.sin(int(input_value))))

    #nusiuncia gauta atsakyma i answer lauka
    answer_input = driver.find_element(By.ID, 'answer')
    answer_input.send_keys(str(result))

    #submitina
    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

driver = webdriver.Chrome()

if __name__ == "__main__":
    solve()
    main_functions()

driver.quit()
