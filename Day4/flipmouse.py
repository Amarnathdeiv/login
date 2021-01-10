import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')


driver.get("http://www.flipkart.com")

flip=driver.find_element_by_xpath("//span[text()='Home & Furniture']")
a=ActionChains(driver)
time.sleep(5)
a.move_to_element(flip).perform()


driver.find_element_by_xpath("//a[@title='Bath Towels']").click()
time.sleep(5)
g=driver.find_element_by_xpath("(//a[contains(text(),'VELHUB')])[1]").text
print(g)


