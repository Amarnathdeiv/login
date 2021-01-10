import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
driver.get("https://www.facebook.com/")
flip=driver.find_element_by_id('email')
flip.send_keys('sdffgf')
a=ActionChains(driver)


a.double_click(flip).perform()
a.context_click(flip).perform()

keyboard.press("down arrow")
keyboard.release("down arrow")
keyboard.press("down arrow")
keyboard.release("down arrow")
keyboard.press("down arrow")
keyboard.release("down arrow")
keyboard.press("Down arrow")
keyboard.release("Down arrow")
keyboard.press("Down arrow")
keyboard.release("Down arrow")

keyboard.press("enter")

keyboard.release("enter")

# keyboard.press("control")
# keyboard.press("A")

# keyboard.press("control")
# keyboard.press("C")

# keyboard.release("control")
# keyboard.release("C")

keyboard.press("tab")
keyboard.release("tab")

keyboard.press("control")
keyboard.press("V")

keyboard.release("control")
keyboard.release("V")

