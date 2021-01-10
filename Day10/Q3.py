from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("https://www.homedepot.com/")

driver.maximize_window()

txt_header=driver.find_element_by_id('headerSearch')

txt_header.send_keys('ceiling fan')

but_search=driver.find_element_by_id('headerSearchButton')

but_search.click()

