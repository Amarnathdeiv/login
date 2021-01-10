from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("https://www.shopclues.com/wholesale.html")

sports=driver.find_element_by_xpath("//a[text()='Sports & More']")

a=ActionChains(driver)

a.move_to_element(sports).perform()

driver.find_element_by_xpath("//a[text()='Weight Gainers']").click()

