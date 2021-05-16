from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class GetemKitap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    def test_download_a_book_from_getem(self):
        driver = self.driver
        driver.get("http://getem.boun.edu.tr/")

        # enter username
        self.username = driver.find_element_by_name("name")
        username = self.username
        username.clear()
        username.send_keys("username")
        time.sleep(1)

        # enter password
        self.password = driver.find_element_by_id("edit-pass")
        password = self.password
        password.clear()
        password.send_keys("password")
        time.sleep(1)

        # checkbox checked
        self.checked = driver.find_element_by_id("edit-remember-me")
        checked = self.checked
        checked.click()
        time.sleep(1)

        # login button clicked
        self.login_button = driver.find_element_by_id("edit-submit")
        login_button = self.login_button
        login_button.click()
        time.sleep(1)
        assert "Katalog" in driver.title

        # type "beyaz" at search box
        self.search_book_name = driver.find_element_by_id("edit-title")
        search_book_name = self.search_book_name
        search_book_name.send_keys("beyaz")
        time.sleep(2)

        # search button clicked
        self.search_button = driver.find_element_by_id("edit-submit-katalog-ara")
        search_button = self.search_button
        search_button.click()
        time.sleep(2)

        # select the book
        self.book = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div[3]/div/"
                                                 "div[3]/div/div/div/div[3]/div[11]/div[1]/span/h2/a")
        book = self.book
        book.click()
        time.sleep(2)

        # download the book
        self.download = driver.find_element_by_id("tumunuindir")
        download = self.download
        download.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()