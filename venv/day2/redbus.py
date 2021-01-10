from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://www.redbus.in/ ')
txt_From=driver.find_element_by_id('src')
txt_From.send_keys('chennai')
txt_To=driver.find_element_by_id('dest')
txt_To.send_keys('pondy')
driver.quit()