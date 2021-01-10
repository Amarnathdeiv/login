from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\geckodriver.exe')
driver.get('https://www.google.com/')
driver.get('http://gmail.com/')
driver.get('http://www.flipkart.com/')
driver.get('http://greenstech.in/selenium-course-content.html')
driver.quit()
