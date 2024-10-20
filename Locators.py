import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Ways to locate an Elements : ID, Name, Class_Name, Link_Text, XPath, CSS_Selector
# Xpath == > //tagname[@propertyName='propertyValue']
# CSSSelector == > tagname[propertyName='propertyValue'] - Same as XPath but without initial slashed & @ symbol before PropertyName
#Apart from Above syntaxes there are easy ways to create a CSS_Selector for ID & Class Attributes of the control
# #IDValue for ID & .ClassName for Class - just Put this value in By.CSS_Selector, "#IDValue" or ".ClassName"


#When there are more than one controls for the same XPath value then to iedntify it uniquely use (XPAth)[3] - will perform action on 3rd element from all possible XPath controls


driver = webdriver.Chrome()
url = r"https://rahulshettyacademy.com/angularpractice/"
driver.get(url)
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Rahul Shetty")
driver.find_element(By.NAME,"email").send_keys("rahulshetty@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(0)
dropdown.select_by_index(1)
dropdown.select_by_index(0)
driver.find_element(By.XPATH, "//label[text()='Employed']").click()
driver.find_element(By.XPATH, "//label[text()='Student']").click()
print(driver.find_element(By.XPATH, "//label[text()='Student']").text)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
#driver.find_element(By.CLASS_NAME, "alert-dismissible")
ActionChains(driver).move_to_element(driver.find_element(By.CLASS_NAME, "alert-dismissible")).perform()
assert "Success!" in msg
time.sleep(3)
