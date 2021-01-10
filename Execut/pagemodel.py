import time

from Framebaseclass.baseclass import Base
from loginpage.pageobject import loging_pg


def login():
    b = Base()
    driver = b.get_browser()
    b.get_url("https://www.facebook.com/")

    log=loging_pg(driver)

    time.sleep(4)

    b.input_txt(log.get_user(), "sele")
    b.input_txt(log.get_pass(), "123")

    b.btn(log.get_bt())

    b.close()


login()
