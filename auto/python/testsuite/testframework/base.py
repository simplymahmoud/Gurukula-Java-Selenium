# -*- coding: utf-8 -*-
import logging
import unittest
import time

from testconfig import config

from pytractor import webdriver
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
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.set_browser()
        self.driver.get(self.environment_url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)

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

    def element_is_enabled(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_enabled()

    def element_is_displayed(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).is_displayed()

    def element_is_readonly(self, element):
        return self.driver.find_element_by_xpath(self.elements[element]).get_attribute("readonly")

    def element_background_color(self, element):
        return str(self.driver.find_element_by_xpath(self.elements[element])\
                   .value_of_css_property('background-color'))

    def wait_until_element_located(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, name)))

    def wait_unti_element_clickable(self, name):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, name)))

    def set_browser(self):
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def click(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        self.wait_unti_element_clickable(element)
        self.driver.find_element_by_xpath(element).click()

    def get_text(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        return self.driver.find_element_by_xpath(element).text

    def get_value(self, element):
        element = self.elements[element]
        self.wait_until_element_located(element)
        return self.driver.find_element_by_xpath(element).get_attribute("value")

    def set_text(self, element, value):
        element = self.elements[element]
        self.wait_until_element_located(element)
        self.driver.find_element_by_xpath(element).clear()
        self.driver.find_element_by_xpath(element).send_keys(value)

    def get_table(self, table):
        table = self.elements[table]
        self.wait_until_element_located(table)
        return self.driver.find_element_by_xpath(table)

    def go_to_login_page(self):
        self.click('login')

    def go_to_register_new_user_page(self):
        self.click('register_new_user')

    def login(self, username='', password='', nopassword=False):
        username = username or self.admin_username
        password = password or self.admin_password
        self.lg('Do login using username [%s] and passsword [%s]' % (username, password))
        self.set_text('username', username)
        if not nopassword:
            self.set_text('password', password)
        self.click('login_button')
        self.lg('Login successfully using username [%s] and passsword [%s]' % (username, password))

    def logout(self):
        self.lg('Do logout')
        self.wait_until_element_located(self.elements['account_menu'])
        self.click('account_menu')
        self.wait_until_element_located(self.elements['logout'])
        self.click('logout')
        self.lg('Logout done successfully')

    def rememberme(self):
        self.click('rememberme')

    def go_to_account_menu(self):
        self.click('account_menu')

    def go_to_account_settings(self):
        self.click('account_settings')

    def go_to_account_passwords(self):
        self.click('account_passwords')

    def click_account_password_save(self):
        self.click('passwords_save_button')

    def click_account_settings_save(self):
        self.click('settings_save_button')

    def register_new_user(self):
        self.click('register_button')

    def click_create_new_branch(self):
        time.sleep(.5)
        self.click('create_new_branch_button')
        time.sleep(.5)

    def click_save_branch(self):
        self.click('save_branch_button')

    def click_cancel_branch(self):
        self.click('cancel_branch_button')

    def click_view_back(self):
        self.click('view_back_button')

    def click_save_edit_branch(self):
        self.click('save_edit_branch_button')

    def click_cancel_edit_branch(self):
        self.click('cancel_edit_branch_button')

    def click_cancel_delete_branch(self):
        self.click('search_branch_cancel_delete')

    def click_create_new_staff(self):
        time.sleep(.5)
        self.click('create_new_branch_button')
        time.sleep(.5)

    def click_staff_next_page(self):
        time.sleep(.5)
        self.click('staff_paging_next_page')
        time.sleep(.5)

    def click_staff_previos_page(self):
        time.sleep(.5)
        self.click('staff_paging_previos_page')
        time.sleep(.5)

    def click_staff_first_page(self):
        time.sleep(.5)
        self.click('staff_paging_first_page')
        time.sleep(.5)

    def click_staff_last_page(self):
        time.sleep(.5)
        self.click('staff_paging_last_page')
        time.sleep(.5)

    def click_save_staff(self):
        self.click('save_staff_button')

    def click_cancel_staff(self):
        self.click('cancel_staff_button')

    def click_save_edit_staff(self):
        self.click('save_edit_staff_button')

    def click_cancel_edit_staff(self):
        self.click('cancel_edit_staff_button')

    def fill_register_new_user(self, login='login', email='email@mail.com', newpasswd=12345,
                               passwdcfm=12345):
        self.set_text('register_login', login)
        self.set_text('register_email', email)
        self.set_text('register_newpasswd', newpasswd)
        self.set_text('register_passwdcfm', passwdcfm)

    def fill_settings(self, firstname='Administrator', lastname='Administrator',
                            email='admin@localhost'):
        self.set_text('settings_firstname', firstname)
        self.set_text('settings_lastname', lastname)
        self.set_text('settings_email', email)

    def fill_passwords(self, newpasswd=12345, passwdcfm=12345):
        self.set_text('passwords_newpasswd', newpasswd)
        self.set_text('passwords_passwdcnf', passwdcfm)

    def create_new_branch(self, name='', code=''):
        name = name or 'BRANCH'
        code = code or '12345'
        self.set_text('new_branch_name', name)
        self.set_text('new_branch_code', code)
        self.name = name
        self.code = code
        time.sleep(.5)
        self.branches.append(name)

    def edit_created_branch(self, name='', code=''):
        name = name or 'branch'
        code = code or '54321'
        self.set_text('edit_branch_name', name)
        self.set_text('new_branch_code', code)
        self.name = name
        self.code = code
        time.sleep(.5)
        self.branches.append(self.name)

    def search_branch(self, name, code=''):
        time.sleep(.5)
        code = code or self.code
        self.set_text('search_branch_text', name)
        self.click('search_branch_button')
        branches_table = self.get_table('search_branch_table')
        tbody = branches_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == name and cells[2].text == code:
                return True

        return False

    def view_branch(self, name, code):
        self.search_branch(name, code)
        branches_table = self.get_table('search_branch_table')
        tbody = branches_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == name and cells[2].text == code:
                cells[3].find_elements_by_tag_name("button")[0].click()
                return True

        return False

    def edit_branch(self, name, code):
        self.search_branch(name, code)
        branches_table = self.get_table('search_branch_table')
        tbody = branches_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == name and cells[2].text == code:
                cells[3].find_elements_by_tag_name("button")[1].click()
                return True

        return False

    def delete_created_branch(self, name):
        self.search_branch(name)
        branches_table = self.get_table('search_branch_table')
        tbody = branches_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        if all_rows:
            cells = all_rows[0].find_elements_by_tag_name("td")
            cells[3].find_elements_by_tag_name("button")[2].click()
            self.click('search_branch_confirm_delete')
            time.sleep(.5)


    def create_new_staff(self, staff='', skip_branch=False):
        staff = staff or 'STAFF'
        self.set_text('new_staff_name', staff)
        if not skip_branch:
            self.wait_until_element_located(self.elements['staff_dropdown'])
            self.driver.find_element_by_xpath(self.elements['staff_dropdown'] + \
            "/option[text()='%s']" % self.name).click()
        self.staff = staff
        time.sleep(.5)
        self.staffs.append(staff)

    def edit_created_staff(self, staff=''):
        staff = staff or 'staff'
        self.set_text('new_staff_name', staff)
        self.staff = staff
        time.sleep(.5)
        self.staffs.append(self.staff)

    def search_staff(self, staff, name=''):
        time.sleep(.5)
        self.set_text('search_branch_text', staff)
        self.click('search_branch_button')
        staff_table = self.get_table('search_branch_table')
        tbody = staff_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == staff and cells[2].text == name:
                return True

        return False

    def view_staff(self, staff, name=''):
        time.sleep(.5)
        self.search_staff(staff, name)
        staff_table = self.get_table('search_branch_table')
        tbody = staff_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == staff and cells[2].text == name:
                cells[3].find_elements_by_tag_name("button")[0].click()
                return True

        return False

    def edit_staff(self, staff, name=''):
        time.sleep(.5)
        self.search_staff(staff, name)
        staff_table = self.get_table('search_branch_table')
        tbody = staff_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        for row in all_rows:
            cells = row.find_elements_by_tag_name("td")
            if cells[1].text == staff and cells[2].text == name:
                cells[3].find_elements_by_tag_name("button")[1].click()
                return True

        return False

    def delete_created_staff(self, staff):
        time.sleep(.5)
        self.search_staff(staff, self.name)
        staff_table = self.get_table('search_branch_table')
        tbody = staff_table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        if all_rows:
            cells = all_rows[0].find_elements_by_tag_name("td")
            cells[3].find_elements_by_tag_name("button")[2].click()
            self.click('search_staff_confirm_delete')
            time.sleep(.5)

    def get_table_count(self, table_name='search_branch_table'):
        table = self.get_table(table_name)
        tbody = table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        return len(all_rows)

    def invalidate_session(self):
        table = self.get_table('account_session_table')
        tbody = table.find_elements_by_tag_name("tbody")
        all_rows = tbody[0].find_elements_by_tag_name("tr")
        if all_rows:
            cells = all_rows[0].find_elements_by_tag_name("td")
            cells[3].find_elements_by_tag_name("button")[0].click()
            time.sleep(.5)

