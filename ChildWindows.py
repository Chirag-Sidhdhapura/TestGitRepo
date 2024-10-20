import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get(r"https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
assert  driver.find_element(By.CSS_SELECTOR, "h3").text == "New Window"
action = ActionChains(driver)
action.context_click(driver.find_element(By.CSS_SELECTOR, "h3")).perform()
time.sleep(3)
driver.close()
driver.switch_to.window(windows[0])
assert  driver.find_element(By.CSS_SELECTOR, "h3").text == "Opening a new window"
action.context_click(driver.find_element(By.CSS_SELECTOR, "h3")).perform()
time.sleep(3)