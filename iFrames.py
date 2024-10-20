import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 1500);")
driver.find_element(By.XPATH, "//fieldset/legend[text()='iFrame Example']").click()
time.sleep(2)

driver.switch_to.frame("courses-iframe")
print("Into Iframe now.....")
#driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES").click()
action = ActionChains(driver)
driver.execute_script("window.scrollTo(0, window.scrollTo(0, document.body.scrollHeight));")
assert driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES").is_displayed()
#action.move_to_element(driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "VIEW ALL COURSES")).perform()
time.sleep(2)