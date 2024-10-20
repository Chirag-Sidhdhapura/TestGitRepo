import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_obj = Service(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://rahulshettyacademy.com")
edgedriver = webdriver.Edge()
edgedriver.get("https://rahulshettyacademy.com")
edgedriver.maximize_window()
title = edgedriver.title
print(type(title), title, sep="**")
print(edgedriver.current_url)
edgedriver.back()

time.sleep(2)

