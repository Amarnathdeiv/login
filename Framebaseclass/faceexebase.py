from Framebaseclass.facexxlsx import Base

#
# class Executable(Base):
#     def login(self):
#         driver=self.get_browser()
#         self.get_url("https://www.facebook.com/")
#         user=driver.find_element_by_id('email')
#         self.input_txt(user,self.excel_read(2,1))
#         pass_txt=driver.find_element_by_id('pass')
#         self.input_txt(pass_txt,self.excel_read(3,4))
#         btnclick=driver.find_element_by_id('u_0_b')
#         self.btn(btnclick)
#         self.close()

# e=Executable()
# e.login()

class Exe:
    def login(self):
        b=Base()
        driver = b.get_browser()
        b.get_url("https://www.facebook.com/")
        user = driver.find_element_by_id('email')
        b.input_txt(user, b.excel_read(2, 1))
        pass_txt = driver.find_element_by_id('pass')
        b.input_txt(pass_txt, b.excel_read(3, 4))
        btnclick = driver.find_element_by_id('u_0_b')
        b.btn(btnclick)

e=Exe()
e.login()