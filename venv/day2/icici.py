from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://infinity.icicibank.com/corp/Login.jsp')
driver.find_element_by_id('DUMMY1').click()
txt_Uid = driver.find_element_by_id('AuthenticationFG.USER_PRINCIPAL')
txt_Uid.send_keys('amarnath')
txt_pass = driver.find_element_by_id('AuthenticationFG.ACCESS_CODE')
txt_pass.send_keys('ssdssd')
driver.quit()