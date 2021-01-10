from selenium import webdriver


class Base:
    def get_browser(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\mohan\PycharmProjects\amarselProject\driver\chromedriver.exe')
        return self.driver

    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def input_txt(self,element,values):
        element.send_keys(values)

    def btn(self,element):
        element.click()

    def close(self):
        self.driver.quit()
