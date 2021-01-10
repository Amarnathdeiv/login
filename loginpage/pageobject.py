from selenium.webdriver.common.by import By

from pom import locators


class loging_pg:
    def __init__(self, driver):
        self.driver = driver
        self.user = self.driver.find_element(By.ID, locators.username_id)
        self.passtxt = self.driver.find_element(By.ID, locators.pass_id)
        self.btn = self.driver.find_element(By.ID, locators.btn_id)

    def get_user(self):
        return (self.user)

    def get_pass(self):
        return (self.passtxt)

    def get_bt(self):
        return (self.btn)
