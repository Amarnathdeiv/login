from Framebaseclass.baseclass import Base


class Executable:
    def call_methods(self):
        b = Base()
        driver = b.get_browser()
        b.get_url("https://www.facebook.com/")

        user_txt = driver.find_element_by_id('email')
        b.input_txt(user_txt, 'amar')
        pass_txt = driver.find_element_by_id('pass')
        b.input_txt(pass_txt, 'am123')
        click_btn = driver.find_element_by_id('u_o_b')
        b.btn(click_btn)
        #b.close()


e = Executable()
e.call_methods()
