import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.homedepot.com/")

all = driver.find_element_by_xpath("(//a[@data-id='departmentsFlyout'])[1]")

a = ActionChains(driver)

a.move_to_element(all).perform()

paint=driver.find_element_by_xpath("(//a[@title='Paint'])[1]")

a.move_to_element(paint).perform()
time.sleep(3)

interior=driver.find_element_by_xpath("(//a[@title='Interior Paint'])[1]")
a.move_to_element(interior).perform()
time.sleep(3)

driver.find_element_by_xpath("//a[text()='Ceiling Paint']").click()