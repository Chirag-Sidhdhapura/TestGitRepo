import time

from selenium import webdriver
#from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
#driver.get(r"https://the-internet.herokuapp.com/iframe")
driver.get(r"https://www.geeksforgeeks.org/")
driver.maximize_window()
#assert driver.find_element(By.XPATH, "//div[text()='Powered by ']").is_displayed()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.get_screenshot_as_file(r"C:\Users\Chirag M. Sidhdhapur\Desktop\Selenium Python\chromedriver-win64\ss.png")

"""
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Updated Text")
driver.switch_to.default_content()"""
time.sleep(3)