import time
from pages.base_page import BasePage
import random

from tests.base_test import BaseTest


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# Locators:
    _greenCart_title = ".brand.greenLogo"
    _product_prices = "p[class='product-price']"
    _all_plus_buttons = "a[class='increment']"
    _all_add_to_cart_buttons = "//button[normalize-space()='ADD TO CART']"
    _addBtn_for_item_with_price = "//p[normalize-space()='{}']/following-sibling::div/button"
    _cartBtn = "a[class='cart-icon']"
    _checkoutBtn = "//button[normalize-space()='PROCEED TO CHECKOUT']"
    _total_amount = ".totAmt"
    _input_promoCode = 'input[class="promoCode"]'
    _apply_promoCodeBtn = "//button[normalize-space()='Apply']"
    _place_orderBtn = "//button[normalize-space()='Place Order']"
    _applying_in_processBtn = "//button[@class='promoBtn' and contains(., 'Applying')]"
    _invalid_promoCode_message = "//span[@class='promoInfo' and contains(., 'Invalid code')]"
    _select_country_dropdown = "select[style]"
    _terms_conditions_checkbox = "input[type='checkbox']"
    _proceed_Btn = "//button[normalize-space()='Proceed']"
    _selectOption_from_selectDropdown = "//option[normalize-space()='Select']"
    _countryOption_from_selectDropdown = "option[value={}]"
    _please_accept_terms_message = "//b[normalize-space()='Please accept Terms & Conditions - Required']"
    _all_countries_in_dropdown = "option[value]"
    _any_country_from_dropdown = "option[value='{}']"
    _actions_section = "//h1[normalize-space()='ACTIONS']"
    _drag_box = "//b[normalize-space()='DRAG ME TO MY TARGET!']"
    _drag_location_element = "//b[normalize-space()='DROP HERE!']"
    _hoverBtn = ".dropdown.hover"
    _link1Btn = "//div[@id='div-hover']/div[1]/div/a"
    _comments_input = "textarea[placeholder='Comments']"
    _successful_purchase = "span[style='color:green;font-size:25px']"


    def verifyHomepageTitleElement(self):
        title = self.isElementPresent(self._greenCart_title, locatorType="css")
        self.log.info("=====> Homepage TEST CASE assertion data is: ")
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
        price = self.get_cheapest_item()
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")

    def select_most_expensive_item(self):
        price = self.get_most_expensive_item()
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")

    def select_third_item(self):
        price = self.get_third_item()
        self.elementClick(self._addBtn_for_item_with_price.format(price), "xpath")

    def goto_cart(self):
        self.elementClick(self._cartBtn)
        self.elementClick(self._checkoutBtn, "xpath")

    def enter_promo_code(self):
        total_amount = self.getText(self._total_amount)
        self.sendKeys(total_amount, self._input_promoCode)
        self.elementClick(self._apply_promoCodeBtn, "xpath")

    def check_promo_code_message(self):
        if self.isElementPresent(self._invalid_promoCode_message, "xpath") is False in range(10):
            time.sleep(1)
            self.log.info("Waiting for promo code confirmation...")
        else:
            return self.isElementPresent(self._invalid_promoCode_message, "xpath")

    def goto_place_order(self):
        self.elementClick(self._place_orderBtn, "xpath")
        time.sleep(1)

    def click_proceed(self):
        self.elementClick(self._proceed_Btn, "xpath")

    def check_terms_err_message(self):
        time.sleep(1)
        self.elementClick(self._proceed_Btn, "xpath")
        time.sleep(1)
        return self.isElementPresent(self._please_accept_terms_message, "xpath")

    def check_disabled_select_option(self):
        return self.isEnabled(self._selectOption_from_selectDropdown, "xpath")

    def select_country_from_dropdown(self):
        allCountries = []
        self.elementClick(self._select_country_dropdown)
        allDropdownOptions = self.getElementList(self._all_countries_in_dropdown)
        for everyCountry in allDropdownOptions:
            country = everyCountry.text
            allCountries.append(country)
        self.log.info(allCountries)
        randomCountry = random.choice(allCountries)
        self.log.info("Random country is: " + randomCountry)
        self.elementClick(self._any_country_from_dropdown.format(randomCountry))
        time.sleep(1)

    def check_successful_purchase(self):
        self.elementClick(self._terms_conditions_checkbox)
        self.click_proceed()
        time.sleep(1)
        successful_page = self.getElement(self._successful_purchase)
        self.log.info(successful_page.text)
        return successful_page.text

    def takeSecondScreenshot(self):
        self.getScreenshot()
        self.driver.switch_to.window(self.driver.window_handles[2])

    def takeFirstScreenshot(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(BaseTest.secondUrl)
        element = self.getElement(self._actions_section, "xpath")
        self.scrollIntoView(element)
        self.webScroll("down")
        self.getScreenshot()
        self.elementClick(self._actions_section, "xpath")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def takePageTitle(self):
        title = self.getTitle()
        self.log.info("=== Title of the page is: " + title + " ===")
        return title

    def dragAndDropBox(self):
        sourceBox = self.getElement(self._drag_box, "xpath")
        targetLocation = self.getElement(self._drag_location_element, "xpath")
        self.dragAndDrop(sourceBox, targetLocation)
        time.sleep(1)

    def hoverOverBtn(self):
        element = self.getElement(self._hoverBtn)
        self.hover(element)

    def confirmLink1_isNot_visible(self):
        return self.isElementDisplayed(self._link1Btn, "xpath")

    def clickLink1(self):
        self.elementClick(self._link1Btn, "xpath")

    def enterTextInComments(self, alert_text):
        time.sleep(1)
        self.sendKeys(alert_text, self._comments_input)

