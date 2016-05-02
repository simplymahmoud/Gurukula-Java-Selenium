# -*- coding: utf-8 -*-
import logging
import unittest
import time
from testconfig import config

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.environment_url = config['main']['url']
        self.admin_username = config['main']['admin']
        self.admin_password = config['main']['passwd']
        self.browser = config['main']['browser']

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = time.time()
        self._logger = logging.LoggerAdapter(logging.getLogger('portal_testsuite'),
                                             {'testid': self.shortDescription() or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.set_browser()
        self.driver.get(self.environment_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 2)

    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        self.driver.quit()
        if hasattr(self, '_startTime'):
            executionTime = time.time() - self._startTime
        self.lg('Testcase %s ExecutionTime is %s sec.' % (self._testID, executionTime))

    def lg(self, msg):
        self._logger.info(msg)

    def go_to_login_page(self):
        self.click('login')

    def go_to_register_new_user_page(self):
        self.click('register_new_user')

    def click(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        self.driver.find_element_by_xpath(element).click()

    def get_text(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        return self.driver.find_element_by_xpath(element).text

    def login(self, username='', password=''):
        username = username or self.admin_username
        password = password or self.admin_password
        self.lg('Do login using username [%s] and passsword [%s]' % (username, password))
        self.wait_until_element_located(self.elements['username'])
        self.driver.find_element_by_xpath(self.elements['username']).clear()
        self.driver.find_element_by_xpath(self.elements['username']).send_keys(username)
        self.driver.find_element_by_xpath(self.elements['password']).clear()
        self.driver.find_element_by_xpath(self.elements['password']).send_keys(password)
        self.click('login_button')
        self.lg('Login successfully using username [%s] and passsword [%s]' % (username, password))

    def logout(self):
        self.lg('Do logout')
        self.wait_until_element_located(self.elements['account_menu'])
        self.click('account_menu')
        self.wait_until_element_located(self.elements['logout'])
        self.click('logout')
        self.lg('Logout done successfully')

    def fill_register_new_user(self, login='login', email='email@mail.com', newpasswd=12345,
                               passwdcfm=12345):
        self.wait_until_element_located(self.elements['register_login'])
        self.driver.find_element_by_xpath(self.elements['register_login']).clear()
        self.driver.find_element_by_xpath(self.elements['register_login']).send_keys(login)
        self.driver.find_element_by_xpath(self.elements['register_email']).clear()
        self.driver.find_element_by_xpath(self.elements['register_email']).send_keys(email)
        self.driver.find_element_by_xpath(self.elements['register_newpasswd']).clear()
        self.driver.find_element_by_xpath(self.elements['register_newpasswd']).send_keys(newpasswd)
        self.driver.find_element_by_xpath(self.elements['register_passwdcfm']).clear()
        self.driver.find_element_by_xpath(self.elements['register_passwdcfm']).send_keys(passwdcfm)

    def register_new_user(self):
        self.wait_until_element_located(self.elements['register_button'])
        self.click('register_button')

    def element_is_enabled(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_enabled()

    def element_is_displayed(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_displayed()

    def element_background_color(self, element):
        return str(self.driver.find_element_by_xpath(self.elements[element])\
                   .value_of_css_property('background-color'))

    def wait_until_element_located(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, name)))

    def set_browser(self):
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        