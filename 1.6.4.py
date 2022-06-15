from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    s=Service('F:\Курсы\Автоматизация тестирования с помощью Selenium и Python\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get(link)

    driver.find_element(By.LINK_TEXT, '224592').click()

    input1 = driver.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()
