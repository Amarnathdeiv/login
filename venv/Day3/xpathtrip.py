
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("https://www.cleartrip.com/trains")
driver.find_element_by_xpath("//a[@href='/register']").click()
driver.find_element_by_id("username1").send_keys("amarnatn007.don@gmail.com")
driver.find_element_by_xpath("//button[@id='registerButton']").click()
time.sleep(5)
driver.find_element_by_css_selector("#password").send_keys("amar@1234")
driver.find_element_by_id("profile_title").send_keys("mr")
driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Amarnath")
driver.find_element_by_xpath("//input[@name='last_name']").send_keys("D")
driver.find_element_by_xpath("//select[@id='country_code']").send_keys("india")
driver.find_element_by_xpath("//input[@title='Phone number']").send_keys(9600077055)
driver.find_element_by_xpath("//button[@id='signUpButton']").click()