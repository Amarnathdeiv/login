from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get('http://demo.automationtesting.in/Register.html')
driver.find_element_by_xpath("(//input[@type='text'])[1]").send_keys("amar")
driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("nath")
driver.find_element_by_xpath("//textarea[@rows='3']").send_keys("vvvchjfcv\zbx c\zc")
driver.find_element_by_xpath("//input[@type='email']").send_keys("amar@gmail")
driver.find_element_by_xpath("//input[@type='tel']").send_keys(9600077055)
#driver.find_element_by_id('msdd').send_keys('English')
#driver.find_element_by_xpath('Skills').send_keys('A')
driver.find_element_by_id('firstpassword').send_keys('asddd')
driver.find_element_by_id('secondpassword').send_keys('asdd')