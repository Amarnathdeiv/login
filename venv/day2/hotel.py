from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('http://adactinhotelapp.com/')
txt_uname=driver.find_element_by_id('username')
txt_uname.send_keys('krish')
txt_pass=driver.find_element_by_id('password')
txt_pass.send_keys('9874632')