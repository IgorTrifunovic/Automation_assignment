import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):

    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    driver.implicitly_wait(5)
    firstUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
    secondUrl = "http://www.webdriveruniversity.com/"
    thirdURL = "http://www.webdriveruniversity.com/Contact-Us/contactus.html"
    driver.maximize_window()
    driver.get(firstUrl)

