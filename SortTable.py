import time

from selenium import webdriver

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)
driver.get(r"https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

fruits = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")

for i in range(len(fruits)-1):
    if not fruits[i].text < fruits[i+1].text:
        print("Values are not sorted")
        break

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
time.sleep(2)

fruits = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
count = 0
list = []

for fruit in fruits:
    list.append(fruit.text)
sortedList = list
print("List is ", list)
print("Sorted List before applying function", sortedList)
sortedList.sort()
print("Sorted List after apppling function", sortedList)
for i in range(len(fruits)-1):
    if fruits[i].text < fruits[i+1].text:
        count += 1
if count == len(fruits)-1:
    print("Values are sorted")
driver.get_screenshot_as_file(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\tablesorted.png")
assert sortedList == list

#print("print statement from user X as an acknowledgement")
print("User X commenting in Develop Branch")