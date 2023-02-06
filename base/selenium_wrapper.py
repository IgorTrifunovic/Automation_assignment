import logging
import time
import traceback
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utilities.custom_logger import customLogger
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import WebDriverException


class SeleniumDriver():
    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False


    def getElement(self, locator, locatorType=""):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except WebDriverException:
            self.log.info("Element raised some of the WebDriverExceptions with locator: " + locator +
                          " and locatorType: " + locatorType)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            # self.log.error("".join(traceback.format_stack()))
        return element

    def getElementList(self, locator, locatorType="css"):
        """
        Get list of elements
        """
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        elements = self.driver.find_elements(byType, locator)
        if len(elements) > 0:
            self.log.info("Element list FOUND with locator: " + locator +
                          " and locatorType: " + locatorType)
        else:
            self.log.info("Element list NOT FOUND with locator: " + locator +
                              " and locatorType: " + locatorType)
        return elements

    def elementClick(self, locator="", locatorType="css",element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            # traceback.print_stack()

    def sendKeys(self, data, locator="", locatorType="css", element=None):
        """
                Send keys to an element -> MODIFIED
                Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            # self.log.error("".join(traceback.format_stack()))

    def getText(self, locator="", locatorType="css", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType="css")
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            # traceback.print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="css", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element_list = self.getElementList(locator, locatorType)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="css", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def getAttributeTitle(self, locator, locatorType=""):
            titleValue = None
            try:
                locatorType = locatorType.lower()
                byType = self.getByType(locatorType)
                titleValue = self.driver.find_element(byType, locator).get_attribute("title")
                self.log.info("Element found with title attribute value!")
            except:
                self.log.info("Element not found with title attribute!")
                self.log.error("Exception Caught: {}".format(traceback.format_exc()))
                # self.log.error("".join(traceback.format_stack()))
                self.log.info("title value is: " + titleValue)
            return titleValue

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1700);")

    def switchToNewWindow(self):
        self.log.info("===== entered switch window =====")
        remote = Remote(self.driver)
        remote.switch_to.alert


    def closeWindow(self):
        remote = Remote(self.driver)
        remote.close()

    def moveSlideBarLeft(self, element, sliderRail):
        move = ActionChains(self.driver)
        time.sleep(1)
        move.click_and_hold(element).move_by_offset(-0.3 * sliderRail.size['width'], 0).release().perform()
        self.log.info("====== executed SeleniumDrivers move slide bar method =======")

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element
        Parameters:
            1. Required:
                1. attribute - attribute whose value to find
            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="css", info=""):
        # Returns:
        #  boolean
        # Exception:
        #     None
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("mkUa-isDisabled" in value)
            if enabled:
                self.log.info("Element :: above is enabled!")
            else:
                self.log.info("Element :: above is disabled.")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled




