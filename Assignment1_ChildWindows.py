import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\chromedriver.exe")
url = r"https://rahulshettyacademy.com/loginpagePractise/"
driver = webdriver.Chrome(service=service_obj)
driver.get(url)
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])

textlist = driver.find_element(By.XPATH, "//div/p[@class='im-para red']").text.split(" ")
for word in textlist:
    if '@' in word:
        emailAddress = word
driver.close()
driver.switch_to.window(windows[0])
driver.find_element(By.ID, "username").send_keys(emailAddress)
driver.find_element(By.ID, "password").send_keys("emailAddress")
roles = driver.find_elements(By.CSS_SELECTOR, ".form-check-inline")
for role in roles:
    if role.get_attribute("value") == "user":
        role.click()
        break
options = Select(driver.find_element(By.XPATH,"//select"))
options.select_by_visible_text("Student")
driver.find_element(By.NAME, "signin").click()
#time.sleep(2)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
errormsg = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(errormsg)
assert "Incorrect" in errormsg

time.sleep(3)