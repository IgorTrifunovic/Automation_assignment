from tests.base_test import BaseTest
from pages.product_page import ProductPage

class HomepageTest(BaseTest):

    def test_homepage(self):
        product_page = ProductPage(BaseTest.driver)
        home_page_title_result = product_page.verifyHomepageTitleElement()
        self.assertTrue(home_page_title_result)

