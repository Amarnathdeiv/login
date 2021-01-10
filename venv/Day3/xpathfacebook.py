from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('https://www.facebook.com/ ')
driver.find_element_by_id('u_0_2').click()
driver.s
driver.find_element_by_id('u_j_b').send_keys("Amar")
driver.find_element_by_id('u_j_d').send_keys("nath")
driver.find_element_by_xpath("//input[@name='reg_email__']").send_keys(123647)
driver.find_element_by_xpath("//input[@name='reg_passwd__']").send_keys('amar123')