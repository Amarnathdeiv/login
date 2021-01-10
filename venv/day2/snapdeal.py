from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://www.snapdeal.com/login')
txt_no=driver.find_element_by_id('userName')
txt_no.send_keys(123654)
