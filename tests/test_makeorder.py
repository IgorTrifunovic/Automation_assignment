import time
from pages.product_page import ProductPage
from selenium import webdriver
from tests.base_test import BaseTest
class MakeOrderTest(BaseTest):

    def test_make_order(self):
        product_page = ProductPage(BaseTest.driver)
        product_page.add_4_same_items_in_cart()
        product_page.select_cheapest_item()
        product_page.select_most_expensive_item()
        product_page.select_third_item()
        product_page.goto_cart()
        product_page.enter_promo_code()
        promo_code_error_message = product_page.check_promo_code_message()
        product_page.goto_place_order()
        disabled_select = product_page.check_disabled_select_option()
        terms_err_message = product_page.check_terms_err_message()
        product_page.select_country_from_dropdown()
        product_page.click_proceed()
        successful_purchase = product_page.check_successful_purchase()
        self.driver.execute_script("window.open()")
        product_page.takeFirstScreenshot()
        product_page.takeSecondScreenshot()
        actions_title_result = product_page.takePageTitle()
        product_page.dragAndDropBox()
        link1_negative_visibility_result = product_page.confirmLink1_isNot_visible()
        product_page.hoverOverBtn()
        link1_positive_visibility_result = product_page.confirmLink1_isNot_visible()
        product_page.clickLink1()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        time.sleep(1)
        self.driver.quit()
        driver2 = webdriver.Chrome()
        driver2.implicitly_wait(5)
        driver2.maximize_window()
        driver2.get(BaseTest.thirdURL)
        product_page = ProductPage(driver2)
        product_page.enterTextInComments(alert_text)
        time.sleep(3)

        self.assertTrue(promo_code_error_message)
        self.assertFalse(disabled_select)
        self.assertTrue(terms_err_message)
        self.assertIn("your order has been placed successfully", successful_purchase)
        self.assertIn("Actions", actions_title_result)
        self.assertFalse(link1_negative_visibility_result)
        self.assertTrue(link1_positive_visibility_result)




