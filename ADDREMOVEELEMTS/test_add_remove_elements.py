import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class AddRemoveElement(unittest.TestCase):

    """http://the-internet.herokuapp.com/add_remove_elements/"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = ("http://the-internet.herokuapp.com/add_remove_elements/")
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertIn(self.base_url, self.driver.current_url)

    def test_add_remove_elements(self):
        "add_remove_elements"
        self.add_element_button = self.driver.find_element_by_css_selector("#content > div > button")
        self.assertTrue(self.add_element_button)
        self.add_element_button.click()
        time.sleep(2)
        self.remove_element_button = self.driver.find_element_by_css_selector("#elements > button")
        self.assertTrue(self.remove_element_button)
        self.remove_element_button.click()
        time.sleep(2)
        self.driver.save_screenshot("add_remove_result.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()