from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get( "https://www.swiggy.com/")
driver.find_element_by_xpath("//a[@class='r2iyh']").click()
driver.find_element_by_id('mobile').send_keys('9600077055')
driver.find_element_by_id('name').send_keys('Amar')
driver.find_element_by_id('email').send_keys('amar@gmail,com')
driver.find_element_by_id('password').send_keys('amanvv123')
