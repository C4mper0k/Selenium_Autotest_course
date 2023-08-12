from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def logs(x):
    return  math.log(abs(12 * math.sin(x)))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем X
    x_def = browser.find_element(By.ID, "input_value").text
    x_num = int(x_def)
    answer = logs(x_num)
    # Ищем поле, скроллим и вставляем ответ (Х)
    field = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(answer)
    # Выбираем чекбокс I'm the robot
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    checkbox1.click()
    # Выбираем радиобатон Robots Rule
    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()
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