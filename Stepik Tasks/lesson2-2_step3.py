from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем Y
    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text
    y = int(x1) + int(x2)

    # Выбираем Y из выпадающего списка
    input1 = Select(browser.find_element(By.TAG_NAME, "select"))
    input1.select_by_value(str(y))

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