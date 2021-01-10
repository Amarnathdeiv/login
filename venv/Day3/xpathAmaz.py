from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("https://www.amazon.in/")
driver.find_element_by_id("nav-link-accountList").click()
driver.find_element_by_id("createAccountSubmit").click()
driver.find_element_by_id('ap_customer_name').send_keys('amar')
driver.find_element_by_xpath("//span[@class='a-button-text a-declarative']").send_keys('in')
driver.find_element_by_id('ap_phone_number').send_keys('9600077055')
driver.find_element_by_id('ap_email').send_keys('amar@gmail.com')
driver.find_element_by_id('ap_password').send_keys('am@th12')
driver.find_element_by_id('continue').click()

