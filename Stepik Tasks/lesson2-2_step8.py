from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поле First name
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Имя")

    # Заполняем поле Last name
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Фамилия")

    # Заполняем поле Email
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    email.send_keys("test@test.com")

    # Прикрепляем файлик
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'first_script.py')
    file_button = browser.find_element(By.ID, 'file')
    file_button.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()