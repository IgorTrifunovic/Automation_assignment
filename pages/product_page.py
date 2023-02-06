import time
from base.selenium_wrapper import SeleniumDriver

class ProductPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators:
    _greenCart_title = ".brand.greenLogo"
    _product_prices = "p[class='product-price']"
    _all_add_product_buttons = "a[class='increment']"

    def verifyHomepageTitleElement(self):
        title = self.isElementPresent(self._greenCart_title, locatorType="css")
        self.log.info(title)
        return title


    def add_4_items_in_cart(self):
        time.sleep(1)
        for x in range(3):
            self.elementClick(self._all_add_product_buttons, "css")
        time.sleep(3)


