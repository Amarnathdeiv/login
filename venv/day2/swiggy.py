from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://www.swiggy.com/')
txt_location=driver.find_element_by_id('location')
txt_location.send_keys('chennai')
#driver.quit()