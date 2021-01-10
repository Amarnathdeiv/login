import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("http://www.greenstechnologys.com/")

dd=driver.find_element_by_link_text("(//p[@style='text-align:justify; font-size:18px;'])[1]")

print(dd)

# a=ActionChains(driver)
#
# a.double_click(dd).perform()
#
# a.context_click(dd).perform()
#
# keyboard.press("down arrow")
# keyboard.release("down arrow")
#
# keyboard.press("down arrow")
# keyboard.release("down arrow")
#
# keyboard.press("down arrow")
# keyboard.release("down arrow")
#
# keyboard.press("enter")
# keyboard.release("enter")