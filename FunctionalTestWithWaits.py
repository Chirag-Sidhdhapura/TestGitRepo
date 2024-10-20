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

for product in products:
    product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//a/img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#tr td:nth-child(5) p ---- //tr/td[5]/p[@class='amount'] -----> CSS_Selector vs XPath
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p[@class='amount']")
total = 0
for amount in amounts:
    total = total+ int(amount.text)

sumAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sumAmount == total

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promoText = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promoText)
assert promoText == "Code applied ..!"

discPercentage = driver.find_element(By.CLASS_NAME, "discountPerc").text
print(discPercentage)
discPercentage = int(discPercentage.replace("%",""))
print(discPercentage)
discAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

discount = sumAmount * discPercentage/100
discAmountCalculated = sumAmount - discount
print(discAmountCalculated)

assert discAmountCalculated == discAmount


