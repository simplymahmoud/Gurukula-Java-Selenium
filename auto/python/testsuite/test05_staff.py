from testframework.base import *
import time
import uuid
from nose_parameterized import parameterized


class StaffTests(BaseTest):

    def setUp(self):
        super(StaffTests, self).setUp()
        self.go_to_login_page()
        self.login()
        time.sleep(.5)
        self.click('entities_menu')
        self.click('entities_branch')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        time.sleep(.5)
        self.click('entities_menu')
        self.click('entities_staff')

    def tearDown(self):
        if hasattr(self, 'staff') and self.staff:
            self.delete_created_staff(self.staff)

        if hasattr(self, 'name') and self.name:
            self.click('entities_menu')
            self.click('entities_branch')
            self.delete_created_branch(self.name)
        super(StaffTests, self).tearDown()

    def test001_create_new_staff(self):
        """ Staff-1: Test case for check create new staff.*

        **Test Scenario:**

        #. do create staff with valid, should succeed
        #. check new staff created successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('%s ENDED' % self._testID)

    def test002_validate_create_new_staff_parameters(self):
        """ Staff-2: Test case for validate create new staff parameters.*

        **Test Scenario:**

        #. click create new staff, should succeed
        #. validate create new staff requirements, should succeed
        #. do create staff with invaild characters, should succeed
        #. validate create new staff requirements, should succeed
        #. proper error message, should succeed
        #. do create staff with invaild max length, should succeed
        #. validate create new staff requirements, should succeed
        #. proper error message, should succeed
        #. do create staff with valid, should succeed
        #. click cancel staff, should succeed
        #. check new staff not created, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('click create new staff, should succeed')
        self.click_create_new_staff()
        self.lg('validate create new branch requirements, should succeed')
        self.assertTrue(self.element_is_readonly('new_staff_id'))
        self.assertTrue(self.element_is_enabled('new_staff_name'))
        self.assertTrue(self.element_is_displayed('new_staff_name_req'))
        self.assertTrue(self.element_is_enabled('staff_dropdown'))
        self.lg('do create staff with invaild characters, should succeed')
        self.create_new_staff('12345')
        self.lg('validate create new staff parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_staff_name_req'))
        self.assertTrue(self.element_is_displayed('new_staff_name_invalid'))
        self.assertFalse(self.element_is_enabled('save_staff_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_staff_name_invalid'),
                         'This field should follow pattern ^[a-zA-Z\s]*$.')
        self.lg('do create staff with invaild max length, should succeed')
        self.create_new_staff('a'*51)
        self.lg('validate create new staff parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_staff_name_req'))
        self.assertFalse(self.element_is_displayed('new_staff_name_invalid'))
        self.assertTrue(self.element_is_displayed('new_staff_name_invalid_maxlength'))
        self.assertFalse(self.element_is_enabled('save_staff_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_staff_name_invalid_maxlength'),
                         'This field cannot be longer than 50 characters.')
        self.lg('do create staff with vaild, should succeed')
        self.create_new_staff()
        self.lg('click cancel branch, should succeed')
        self.click_cancel_staff()
        self.lg('check new branch not created, should succeed')
        self.assertFalse(self.search_staff(self.staff))
        self.lg('%s ENDED' % self._testID)

    def test003_view_delete_staff(self):
        """ Staff-3: Test case for check view/delete staff.*

        **Test Scenario:**

        #. do create staff with valid, should succeed
        #. check new staff created successfully, should succeed
        #. view staff with valid, should succeed
        #. check new staff updated successfully, should succeed
        #. delete staff, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create staff with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('view staff with name, should succeed')
        self.assertTrue(self.view_staff(self.staff, self.name))
        self.assertTrue(self.element_is_readonly('search_staff_view_name'))
        self.assertTrue(self.element_is_readonly('search_staff_view_branch'))
        self.assertEqual(self.get_value('search_staff_view_name'), self.staff)
        self.assertEqual(self.get_value('search_staff_view_branch'), self.name)
        self.click_view_back()
        self.lg('delete staff, should succeed')
        self.delete_created_staff(self.staff)
        self.assertFalse(self.search_staff(self.staff))
        self.lg('%s ENDED' % self._testID)

    def test004_edit_delete_staff(self):
        """ Staff-4: Test case for check edit/delete created staff.*

        **Test Scenario:**

        #. do create staff with valid, should succeed
        #. check new staff created successfully, should succeed
        #. edit staff with valid, should succeed
        #. check new staff updated successfully, should succeed
        #. delete staff, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create staff with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('edit staff with valid, should succeed')
        self.edit_staff(self.staff, self.name)
        self.edit_created_staff()
        self.click_save_edit_staff()
        self.lg('check new staff updated successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('delete staff, should succeed')
        self.delete_created_staff(self.staff)
        self.assertFalse(self.search_staff(self.staff))
        self.lg('%s ENDED' % self._testID)

    def test005_validate_edit_staff_parameters(self):
        """ Staff-5: Test case for validate create edit staff parameters.*

        **Test Scenario:**

        #. click create new staff, should succeed
        #. validate create new staff requirements, should succeed
        #. edit staff with invaild characters, should succeed
        #. validate create new staff requirements, should succeed
        #. proper error message, should succeed
        #. edit staff with invaild max length, should succeed
        #. validate create new staff requirements, should succeed
        #. proper error message, should succeed
        #. do create staff with valid, should succeed
        #. click cancel edit staff, should succeed
        #. check created staff not updated, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create staff with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        start_staff = self.staff
        self.edit_staff(self.staff, self.name)
        self.lg('validate create new staff requirements, should succeed')
        self.set_text('new_staff_name', '')
        self.assertTrue(self.element_is_readonly('new_staff_id'))
        self.assertTrue(self.element_is_enabled('new_staff_name'))
        self.assertTrue(self.element_is_displayed('new_staff_name_req'))
        self.lg('edit staff with invaild characters, should succeed')
        self.edit_created_staff('12345')
        self.lg('validate create new staff parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_staff_name_req'))
        self.assertTrue(self.element_is_displayed('new_staff_name_invalid'))
        self.assertFalse(self.element_is_enabled('save_staff_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_staff_name_invalid'),
                         'This field should follow pattern ^[a-zA-Z\s]*$.')
        self.lg('edit staff with invaild max length, should succeed')
        self.edit_created_staff('a'*51)
        self.lg('validate create new staff parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_staff_name_invalid'))
        self.assertTrue(self.element_is_displayed('new_staff_name_invalid_maxlength'))
        self.assertFalse(self.element_is_enabled('save_staff_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_staff_name_invalid_maxlength'),
                         'This field cannot be longer than 50 characters.')
        self.lg('edit staff with vaild, should succeed')
        self.edit_created_staff()
        self.lg('click cancel staff, should succeed')
        self.click_cancel_staff()
        self.lg('check new staff not updated, should succeed')
        self.assertFalse(self.search_staff(self.staff))
        self.assertTrue(self.search_staff(start_staff))
        self.lg('%s ENDED' % self._testID)

    def test006_validate_search_delete_staff(self):
        """ Staff-6: Test case for validate search/delete staff.*

        **Test Scenario:**

        #. do create new staff, should succeed
        #. search new staff, should succeed
        #. delete staff, should succeed
        #. search new staff, should fail
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new staff, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('search new branch, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('delete staff, should succeed')
        self.delete_created_staff(self.staff)
        self.lg('search new staff, should fail')
        self.assertFalse(self.search_staff(self.staff))
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal name', str(uuid.uuid4())),
                           ('long name', 'X'*1000),
                           ('numeric name', 9876543210),
                           ('special chars name', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test007_validate_search_delete_invalid_staff(self, _, name):
        """ Staff-7: Test case for validate search/delete invalid staff.*

        **Test Scenario:**

        #. do create new staff, should succeed
        #. search invalid staff, should fail
        #. delete staff, should succeed
        #. search invalid staff, should fail
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new staff, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('search invalid staff, should fail')
        self.assertFalse(self.search_staff(name))
        self.lg('delete staff, should succeed')
        self.delete_created_staff(self.staff)
        self.lg('search invalid staff, should fail')
        self.assertFalse(self.search_staff(name))
        self.lg('%s ENDED' % self._testID)
