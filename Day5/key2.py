from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("https://www.google.co.in/webhp ")

doclick=driver.find_element_by_xpath("(//a[@class='gb_g'])[1]")

a=ActionChains(driver)

a.double_click(doclick).perform()