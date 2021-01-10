import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("http://www.amazon.in")

prime=driver.find_element_by_xpath("(//div[@class='nav-line-1-container'])[2]")

a=ActionChains(driver)
a.move_to_element(prime).perform()

time.sleep(5)

driver.find_element_by_xpath("//img[@id='multiasins-img-link']").click()