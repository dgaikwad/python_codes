#!/usr/bin/python
""" This program will search "pycon" keyword on provided site and validate test as per search result. """


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class pythonorgserach(unittest.TestCase):

    def setUp(self):

	"""set geckodriver bin file path """
        self.driver = webdriver.Firefox(executable_path = "/home/devi/web/geckodriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        ele = driver.find_element_by_name("q")
        ele.send_keys("pycon")
        ele.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



