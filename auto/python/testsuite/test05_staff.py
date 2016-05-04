from testframework.base import *
import uuid
import time
from nose_parameterized import parameterized


class StaffTests(BaseTest):

    def setUp(self):
        super(StaffTests, self).setUp()
        self.branches = []
        self.staffs = []
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
            for staff in self.staffs:
                self.search_staff(staff)
                self.delete_created_staff(staff)


        if hasattr(self, 'name') and self.name:
            self.click('entities_menu')
            self.click('entities_branch')
            for branch in self.branches:
                self.search_branch(branch, self.code)
                self.delete_created_branch(name=branch)
                    

        super(StaffTests, self).tearDown()

    def test001_create_new_staff(self):
        """ Staff-1: Test case for check create new staff.*

        **Test Scenario:**

        #. do create staff with valid, should succeed
        #. check new staff created successfully, should succeed
        #. do create staff without branch, should succeed
        #. check new staff created successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('do create branch without branch, should succeed')
        self.click_create_new_staff()
        self.create_new_staff(skip_branch=True)
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
        self.create_new_staff(skip_branch=True)
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('view staff with name, should succeed')
        self.assertTrue(self.view_staff(self.staff))
        self.assertTrue(self.element_is_readonly('search_staff_view_name'))
        self.assertTrue(self.element_is_readonly('search_staff_view_branch'))
        self.assertEqual(self.get_value('search_staff_view_name'), self.staff)
        self.assertEqual(self.get_value('search_staff_view_branch'), '')
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
        self.create_new_staff(skip_branch=True)
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('edit staff with valid, should succeed')
        self.edit_staff(self.staff, '')
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
        self.create_new_staff(skip_branch=True)
        self.click_save_staff()
        self.lg('check new staff created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        start_staff = self.staff
        self.edit_staff(self.staff)
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
        self.create_new_staff(skip_branch=True)
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
        self.create_new_staff(skip_branch=True)
        self.click_save_staff()
        self.lg('search invalid staff, should fail')
        self.assertFalse(self.search_staff(name))
        self.lg('delete staff, should succeed')
        self.delete_created_staff(self.staff)
        self.lg('search invalid staff, should fail')
        self.assertFalse(self.search_staff(name))
        self.lg('%s ENDED' % self._testID)

    def test008_create_new_staff(self):
        """ Staff-8: Test case for check staff paging.*

        **Test Scenario:**

        #. create multiple staff with valid, should succeed
        #. check paging is working successfully, should succeed
        #. check paging size is 20 record per page, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('create multiple staff with valid, should succeed')
        for _ in range(50):
            self.click_create_new_staff()
            self.create_new_staff(skip_branch=True)
            self.click_save_staff()

        self.lg('check paging is working successfully, should succeed')
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertFalse(self.element_is_displayed('staff_paging_previos_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.lg('check paging size is 20 record per page, should succeed')
        self.assertEqual(self.get_table_count(), 20)
        self.click_staff_next_page()
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_previos_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.assertEqual(self.get_table_count(), 20)
        self.click_staff_next_page()
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_previos_page'))
        self.assertFalse(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.assertEqual(self.get_table_count(), 10)
        self.click_staff_previos_page()
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_previos_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.assertEqual(self.get_table_count(), 20)
        self.click_staff_first_page()
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertFalse(self.element_is_displayed('staff_paging_previos_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.assertEqual(self.get_table_count(), 20)
        self.click_staff_last_page()
        time.sleep(1)
        self.assertTrue(self.element_is_displayed('staff_paging_first_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_previos_page'))
        self.assertFalse(self.element_is_displayed('staff_paging_next_page'))
        self.assertTrue(self.element_is_displayed('staff_paging_last_page'))
        self.assertEqual(self.get_table_count(), 10)
        self.lg('%s ENDED' % self._testID)

    def test009_delete_used_branch_before_staff(self):
        """ Staff-9: Test case for check delete used branch before staff.*

        **Test Scenario:**

        #. do create staff with valid, should succeed
        #. check new staff created successfully, should succeed
        #. try delete branch before staff, should fail
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_staff()
        self.create_new_staff()
        self.click_save_staff()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_staff(self.staff))
        self.lg('try delete branch before staff, should fail')
        self.click('entities_menu')
        self.click('entities_branch')
        self.delete_created_branch(self.name)
        self.click_cancel_delete_branch()
        self.assertEqual(self.get_table_count(), 1)
        time.sleep(1)
        self.click('entities_menu')
        self.click('entities_staff')
        self.lg('%s ENDED' % self._testID)

    def test010_delete_not_used_branch_before_staff(self):
        """ Staff-10: Test case for check delete not used branch before staff.*

        **Test Scenario:**

        #. do create staff without branch, should succeed
        #. delete branch before staff, should succeed
        #. delete staff, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch without branch, should succeed')
        self.click_create_new_staff()
        self.create_new_staff(skip_branch=True)
        self.click_save_staff()
        self.lg('delete branch before staff, should succeed')
        time.sleep(1)
        self.click('entities_menu')
        self.click('entities_branch')
        self.delete_created_branch(self.name)
        self.assertEqual(self.get_table_count(), 0)
        self.click('entities_menu')
        self.click('entities_staff')
        self.delete_created_staff(self.staff)
        self.lg('%s ENDED' % self._testID)

    def test011_validate_search_different_staff(self):
        """ Staff-11: Test case for validate search different staff.

        **Test Scenario:**

        #. do create new staff1, should succeed
        #. search new staff1, should succeed
        #. do create new staff2, should succeed
        #. search new staff2, should succeed
        #. search new staff1, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new staff1, should succeed')
        staff_1 = 'staffa'
        for _ in range(2):
            self.click_create_new_staff()
            self.create_new_staff(staff_1)
            self.click_save_staff()

        self.lg('search new staff1, should succeed')
        time.sleep(1)
        self.search_staff(staff_1)
        self.assertEqual(self.get_table_count(), 2)
        self.lg('do create new staff1, should succeed')
        staff_2 = 'staffb'
        for _ in range(3):
            self.click_create_new_staff()
            self.create_new_staff(staff_2)
            self.click_save_staff()

        self.lg('search new staff1, should succeed')
        time.sleep(1)
        self.search_staff(staff_2)
        self.assertEqual(self.get_table_count(), 3)
        self.lg('search new staff1, should succeed')
        time.sleep(1)
        self.search_staff(staff_1)
        self.assertEqual(self.get_table_count(), 2)
        self.lg('%s ENDED' % self._testID)

