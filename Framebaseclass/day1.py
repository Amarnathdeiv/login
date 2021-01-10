import unittest


class Emp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("before class")

    @classmethod
    def tearDownClass(cls):
        print("after class")

    def setUp(self):
        print("before method")

    def tearDown(self):
        print("after method")

    def test_log(self):
        print("payment")

    def test_login(self):
        print("Login")


    unittest.main()



