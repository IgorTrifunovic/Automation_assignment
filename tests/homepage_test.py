import time

from pages.product_page import ProductPage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HomepageTest(unittest.TestCase):
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    # chrome_opt.add_experimental_option("detach", True)   # stop teardown by detaching current session
    driver = webdriver.Chrome(options=chrome_opt)
    driver.implicitly_wait(5)
    firstUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
    driver.maximize_window()
    driver.get(firstUrl)
    prp = ProductPage(driver)


    def test_homepage(self):
        assert self.prp.verifyHomepageTitleElement()

    def test_make_order(self):
        self.prp.add_4_same_items_in_cart()
        self.prp.select_cheapest_item()
        self.prp.select_most_expensive_item()
        self.prp.select_third_item()
        self.prp.goto_cart()
        self.prp.enter_promo_code()
        promo_code_error_message = self.prp.check_promo_code_message()
        self.prp.goto_place_order()
        self.prp.use_select_country_dropdown()
        disabled_select_option = self.prp.check_is_first_select_option_disabled()






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





