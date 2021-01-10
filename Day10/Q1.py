import time

import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')


driver.get("https://www.amazon.in/")

search_txt=driver.find_element_by_id("twotabsearchtextbox")
search_txt.send_keys("iphone x")

search_clk=driver.find_element_by_xpath("(//input[@type='submit'])[1]")

search_clk.click()

iphone_rightclick=driver.find_element_by_xpath("(//span[text()='Apple iPhone Xs (512GB) - Space Grey'])[1]")

a=ActionChains(driver)

a.context_click(iphone_rightclick).perform()
time.sleep(3)
keyboard.press("down arrow")
keyboard.release("down arrow")

keyboard.press("enter")
keyboard.release("enter")
time.sleep(5)
child=driver.window_handles[1]
driver.switch_to.window(child)
quantity=driver.find_element_by_id("quantity")

s = Select(quantity)
s.select_by_visible_text("2")





