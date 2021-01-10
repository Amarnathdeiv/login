import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("http://greenstech.in/selenium-course-content.html")

course=driver.find_element_by_xpath("//div[@title='Courses'] ")
a1=ActionChains(driver)
a1.move_to_element(course).perform()
time.sleep(3)

sel=driver.find_element_by_xpath("//span[text()='Software Testing (12)']")

a1.move_to_element(sel).perform()

ssel=driver.find_element_by_xpath("//span[text()='Selenium Certification Training']").click()

