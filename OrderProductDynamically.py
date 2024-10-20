import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#XPATH -> //a[contains(@href,'shop')]
#CSS_Selector -> a[href*='shop']

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get(r"https://rahulshettyacademy.com/angularpractice/shop")
wishlist = ["iphone X", "Blackberry"]
cost = 0
time.sleep(5)
"""
products = driver.find_elements(By.CSS_SELECTOR, "app-card")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for product in products:
    if product.find_element(By.CSS_SELECTOR, "h4").text == "Blackberry":
        print(driver.find_element(By.CSS_SELECTOR, "p").text)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        driver.find_element(By.CSS_SELECTOR, "button").click()


driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click() """














products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
for product in products:
    if product.find_element(By.XPATH, "div/h4").text in wishlist:
        cost = cost + float(product.find_element(By.XPATH, "div/h5").text.replace("$",""))
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
print(cost)

driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.ID, "country").send_keys("Ind")
WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
successsmg = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
print(successsmg)
assert "Success! Thank you" in successsmg
time.sleep(5)