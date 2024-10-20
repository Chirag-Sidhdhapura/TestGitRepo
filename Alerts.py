import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url=r"https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys("Chirag")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert "Chirag" in alertText

time.sleep(3)
alert.accept()
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
time.sleep(3)
driver.switch_to.alert
print(alert.text)
alert.dismiss()
time.sleep(3)