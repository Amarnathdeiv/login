from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("http://greenstech.in/selenium-course-content.html")
driver.find_element_by_id("heading881").click()
