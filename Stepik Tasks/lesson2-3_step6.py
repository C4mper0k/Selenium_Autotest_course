from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def logs(x):
    return  math.log(abs(12 * math.sin(x)))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_prev = browser.find_element(By.TAG_NAME, "button")
    button_prev.click()

    # Переключаемся на новую вкладку. Так же работает browser.switch_to.window(new_window)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Вычисляем X
    x_def = browser.find_element(By.ID, "input_value").text
    x_num = int(x_def)
    answer = logs(x_num)

    # Ищем поле, скроллим и вставляем ответ (Х)
    field = browser.find_element(By.ID, "answer")
    field.send_keys(answer)
    
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