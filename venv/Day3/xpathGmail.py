from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
driver.find_element_by_id('firstName').send_keys('amar')
driver.find_element_by_id('lastName').send_keys('nath')
driver.find_element_by_id('username').send_keys('amar123')
driver.find_element_by_xpath("(//input[@type='password'])[1]").send_keys('ama1236')
driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys('ama1236')
