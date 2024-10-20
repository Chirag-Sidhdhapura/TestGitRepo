import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
url = r"https://rahulshettyacademy.com/client"
driver.get(url)
driver.maximize_window()
driver.title
driver.current_url
driver.find_element(By.CSS_SELECTOR,".forgot-password-link").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your email address']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.implicitly_wait(5)
msg = driver.find_element(By.CSS_SELECTOR, ".toast-title").click()
msg = driver.find_element(By.CSS_SELECTOR, ".toast-title").text
assert msg in "Password Changed Successfully"




time.sleep(5)