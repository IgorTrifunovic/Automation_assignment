import time
from base.selenium_wrapper import SeleniumDriver

class ProductPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators:
    _greenCart_title = ".brand.greenLogo"
    _product_prices = "p[class='product-price']"
    _all_plus_buttons = "a[class='increment']"
    _all_add_to_cart_buttons = "//button[normalize-space()='ADD TO CART']"  # xpath
    _addBtn_for_item_with_price = "//p[normalize-space()='{}']/following-sibling::div/button"  # xpath
    _cartBtn = "a[class='cart-icon']"
    _checkoutBtn = "//button[normalize-space()='PROCEED TO CHECKOUT']"  # xpath
    _total_amount = ".totAmt"
    _input_promoCode = 'input[class="promoCode"]'
    _apply_promoCodeBtn = "//button[normalize-space()='Apply']"   # xpath
    _place_orderBtn = "//button[normalize-space()='Place Order']"   # xpath
    _applying_in_processBtn = "//button[@class='promoBtn' and contains(., 'Applying')]"  # xpath
    _invalid_promoCode_message = "//span[@class='promoInfo' and contains(., 'Invalid code')]"  # xpath
    _select_country_dropdown = "select[style]"
    _terms_conditions_checkbox = "input[type='checkbox']"
    _proceed_placeOrderBtn = "//button[normalize-space()='Proceed']"   # xpath
    _selectOption_from_selectDropdown = "//option[normalize-space()='Select']"   # xpath
    _countryOption_from_selectDropdown = "option[value={}]"
    _please_accept_terms_message = "//b[normalize-space()='Please accept Terms & Conditions - Required']"  # xpath



    def verifyHomepageTitleElement(self):
        title = self.isElementPresent(self._greenCart_title, locatorType="css")
        self.log.info(title)
        return title


    def add_4_same_items_in_cart(self):
        time.sleep(1)
        for x in range(3):
            self.elementClick(self._all_plus_buttons, "css")
        self.elementClick(self._all_add_to_cart_buttons, "xpath")
        time.sleep(1)

    def get_visible_prices(self):
        prices_strings = []
        all_prices = self.getElementList(self._product_prices, "css")
        for eachPrice in all_prices:
            if eachPrice is not None:
                one_price = eachPrice.text
                prices_strings.append(one_price)
            else:
                self.log.info("==== Prices after price filter are None!!! =====")
        return prices_strings

    def get_cheapest_item(self):
        pricesInt = []
        time.sleep(1)
        pricesStr = list(filter(None, self.get_visible_prices()))
        for each in pricesStr:
            pricesInt.append(int(each))
            pricesInt.sort()
        return pricesInt[0]

    def get_most_expensive_item(self):
        pricesInt = []
        pricesStr = list(filter(None, self.get_visible_prices()))
        for each in pricesStr:
            pricesInt.append(int(each))
            pricesInt.sort()
        return pricesInt[-1]

    def get_third_item(self):
        pricesInt = []
        pricesStr = list(filter(None, self.get_visible_prices()))
        for each in pricesStr:
            pricesInt.append(int(each))
            pricesInt.sort()
        return pricesInt[-3]

    def select_cheapest_item(self):
        price = self.get_cheapest_item()    # check is locator Int sensitive / it is not
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")
        time.sleep(1)

    def select_most_expensive_item(self):
        price = self.get_most_expensive_item()
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")
        time.sleep(1)

    def select_third_item(self):
        price = self.get_third_item()
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")
        time.sleep(1)

    def goto_cart(self):
        self.elementClick(self._cartBtn)
        time.sleep(1)
        self.elementClick(self._checkoutBtn, "xpath")

    def enter_promo_code(self):
        time.sleep(1)
        total_amount = self.getText(self._total_amount)
        self.log.info(total_amount)
        self.sendKeys(total_amount, self._input_promoCode)
        self.elementClick(self._apply_promoCodeBtn, "xpath")
        time.sleep(1)

    def check_promo_code_message(self):
        for x in range(20):
            if self.isElementPresent(self._applying_in_processBtn, "xpath") is True:
                time.sleep(0.5)
                self.log.info("Waiting for promo code confirmation...")
            else:
                return self.isElementPresent(self._invalid_promoCode_message, "xpath")
        time.sleep(3)

    def goto_place_order(self):
        time.sleep(1)
        self.elementClick(self._place_orderBtn, "xpath")
        time.sleep(3)

    def check_is_first_select_option_disabled(self):
        time.sleep(2)
        selectOption = self.isEnabled(self._selectOption_from_selectDropdown, "xpath")
        if selectOption is False:
            return True
        else:
            return False

    def use_select_country_dropdown(self):
        self.elementClick(self._select_country_dropdown)



