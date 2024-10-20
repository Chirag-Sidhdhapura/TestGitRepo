import time
from tabnanny import check

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#url = r"https://rahulshettyacademy.com/dropdownsPractise/"
url = r"https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
"""driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type to Select']").send_keys("ind")
time.sleep(2)
dropdowns = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
#print(dropdowns)
for dropdown in dropdowns:
    if dropdown.text == "India":
        dropdown.click()

assert driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type to Select']").get_attribute("value") == "India"
"""

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break

assert driver.find_element(By.XPATH, "//input[@placeholder='Hide/Show Example']").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

#assert driver.find_element(By.XPATH, "//input[@placeholder='Hide/Show Example']").is_displayed() == False
assert not driver.find_element(By.XPATH, "//input[@placeholder='Hide/Show Example']").is_displayed()




time.sleep(3)