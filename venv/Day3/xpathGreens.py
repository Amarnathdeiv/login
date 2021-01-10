from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('http://www.greenstechnologys.com/')
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='CONTACT US']").click()
driver.find_element_by_id('InputName').send_keys("Amarnath")
driver.find_element_by_xpath("//input[@name='email'][1]").send_keys("amr@133")
driver.find_element_by_xpath("(//input[@class='form-control'])[3]").send_keys(123567)
driver.find_element_by_xpath("(//select[@name='courses'])[1]").send_keys("selenium")
driver.find_element_by_xpath("(//select[@class='form-control'])[2]").send_keys("T")
driver.find_element_by_xpath("(//select[@name='time'])[1]").send_keys("I")
driver.find_element_by_xpath("(//textarea[@name='comments'])[1]").send_keys("Best Training institute in chennai")
