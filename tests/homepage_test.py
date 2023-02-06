import time

from pages.product_page import ProductPage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HomepageTest(unittest.TestCase):
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    # chrome_opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_opt)
    driver.implicitly_wait(5)
    firstUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
    driver.maximize_window()
    driver.get(firstUrl)
    prp = ProductPage(driver)


    def test_homepage(self):
        assert self.prp.verifyHomepageTitleElement()

    def test_order(self):
        self.prp.add_4_items_in_cart()







    def test_newtab(self):
        secondUrl = "http://www.webdriveruniversity.com/"
        driver = HomepageTest.driver
        asd = driver.window_handles
        print(asd)
        self.driver.execute_script("window.open()")
        asd = driver.window_handles
        print(asd)
        self.driver.switch_to.window(asd[1])
        self.driver.get(secondUrl)
        time.sleep(2)
        self.driver.switch_to.window(asd[0])
        time.sleep(2)





