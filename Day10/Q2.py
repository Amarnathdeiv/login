import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')

driver.get("https://www.snapdeal.com/")


Txt_search=driver.find_element_by_id('inputValEnter')

Txt_search.send_keys('samsung mobiles')

Ent_search=driver.find_element_by_xpath("//span[text()='Search']")

Ent_search.click()

time.sleep(5)

pro_click=driver.find_element_by_xpath("//p[contains(text(),'Bhavi HBS 730 For Redmi')]")

pro_click.click()
time.sleep(5)

child=driver.window_handles[1]
driver.switch_to.window(child)

add_cart=driver.find_element_by_id('add-cart-button-id')

add_cart.click()

