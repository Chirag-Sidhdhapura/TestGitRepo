import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(r"https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.implicitly_wait(5)
rows = driver.find_elements(By.CSS_SELECTOR, ".rdt_TableRow")
"""

for row in rows:
    cells = row.find_elements(By.CSS_SELECTOR, ".rdt_TableCell")
    for cell in cells :
        print(cell.text, end=" - ")
    print()
"""
#driver.find_element(By.ID, "downloadButton")
driver.find_element(By.ID, "fileinput").send_keys(r"C:\Users\Chirag M. Sidhdhapur\Downloads\download.xlsx")
#WebDriverWait(driver, 15).until(ec.invisibility_of_element()(By.XPATH, "//div[text()='Updated Excel Data Successfully.']")))
#WebDriverWait.until(ec.invisibility_of_element_located())
WebDriverWait(driver, 15).until(ec.invisibility_of_element_located((By.XPATH, "//div[text()='Updated Excel Data Successfully.']")))
driver.find_element(By.TAG_NAME, "h1").click()
driver.find_element(By.XPATH, "//div[text()='Updated Excel Data Successfully.']")

WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text()='Fruit Name']")))
fruitColNum = driver.find_element(By.XPATH, "//div[text()='Fruit Name']").get_attribute("data-column-id")
for row in rows:
    #locator = (By.XPATH, "div[]")
    temp = (By.CSS_SELECTOR, "div[role='cell']:nth-child(2)")
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((temp)))
    if row.find_element(*temp).text == "Apple":
        print(row.find_element(By.XPATH, "div[5]").text)

time.sleep(5)