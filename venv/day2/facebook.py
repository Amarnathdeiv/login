from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://www.facebook.com/ ')
txt_Uname=driver.find_element_by_id('email')
txt_Uname.send_keys('amar')
txt_Pass=driver.find_element_by_id('pass')
txt_Pass.send_keys(32365)
driver.quit()