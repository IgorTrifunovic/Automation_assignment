import time
from pages.product_page import ProductPage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

alert_text = None
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
        asd = self.prp.verifyHomepageTitleElement()
        print("===== TEST CASE 1: ")
        print(asd)
        assert asd

    def test_make_order(self):
        print("===== TEST CASE 2: ")
        self.prp.add_4_same_items_in_cart()
        self.prp.select_cheapest_item()
        self.prp.select_most_expensive_item()
        self.prp.select_third_item()
        self.prp.goto_cart()
        self.prp.enter_promo_code()
        promo_code_error_message = self.prp.check_promo_code_message()              # Assert data
        self.prp.goto_place_order()
        disabled_select = self.prp.check_disabled_select_option()                   # Assert data
        terms_err_message = self.prp.check_terms_err_message()                      # Assert data
        self.prp.select_country_from_dropdown()
        self.prp.click_proceed()
        global alert_text
        secondUrl = "http://www.webdriveruniversity.com/"
        driver = HomepageTest.driver
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(driver.window_handles[1])
        self.driver.get(secondUrl)
        self.prp.takeActionsScreenshot()
        self.driver.switch_to.window(driver.window_handles[1])
        self.prp.takeScreenshot()
        time.sleep(2)
        self.driver.switch_to.window(driver.window_handles[2])
        actions_title_result = self.prp.takePageTitle()                             # Assert data
        self.prp.dragAndDropBox()
        link1_negative_visibility_result = self.prp.confirmLink1_isNot_visible()    # Assert data
        self.prp.hoverOverBtn()
        link1_positive_visibility_result = self.prp.confirmLink1_isNot_visible()    # Assert data
        self.prp.clickLink1()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        thirdURL = "http://www.webdriveruniversity.com/Contact-Us/contactus.html"
        driver = HomepageTest.driver
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(driver.window_handles[1])
        self.driver.get(thirdURL)
        self.prp.enterTextInComments(alert_text)
        time.sleep(3)

        print(promo_code_error_message)
        print(disabled_select)
        print(terms_err_message)
        print(actions_title_result)
        print(link1_negative_visibility_result)
        print(link1_positive_visibility_result)
        print(alert_text)

