import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.homedepot.com/")

all = driver.find_element_by_xpath("(//a[@data-id='departmentsFlyout'])[1]")

a = ActionChains(driver)

a.move_to_element(all).perform()

heat = driver.find_element_by_xpath("//a[text()='Heating & Cooling']")
time.sleep(5)
a.move_to_element(heat).perform()
time.sleep(5)
cond = driver.find_element_by_xpath("//a[@title='Air Conditioners']")
#time.sleep(6)
a.move_to_element(cond).perform()

time.sleep(3)
port = driver.find_element_by_xpath("//a[text()='Portable Air Conditioners']")

port.click()
