from itertools import product

from selenium import webdriver

l = ["Cucumber", "Raspberry", "Strawberry"]
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = "https://rahulshettyacademy.com/seleniumPractise/#/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)

products = driver.find_elements(By.XPATH, "//div[@class='product']")
productlist = []
for product in products:
    productname = product.find_element(By.XPATH, "h4").text
    productname = productname.split(" - ")[0]
    productlist.append(productname)
print(productlist)

print(l == productlist)