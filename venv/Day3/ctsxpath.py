from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("http://greenstech.in/selenium-course-content.html")
driver.find_element_by_xpath("//div[@id='heading20']").click()
ctsLink = driver.find_element_by_xpath("//a[text()='CTS Interview Question ']").click()
print(ctsLink)

