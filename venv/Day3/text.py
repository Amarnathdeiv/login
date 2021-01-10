from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("http://www.greenstechnologys.com/")
content = driver.find_element_by_xpath("(//p[@style='text-align:justify; font-size:18px;'])[3]")
print(content.text)
