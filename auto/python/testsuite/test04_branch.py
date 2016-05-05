from testframework.base import *
import uuid
from nose_parameterized import parameterized


class BranchTests(BaseTest):

    def setUp(self):
        super(BranchTests, self).setUp()
        self.branches = []
        self.go_to_login_page()
        self.login()
        self.click('entities_menu')
        self.click('entities_branch')

    def tearDown(self):
        if hasattr(self, 'name') and self.name:
            for branch in self.branches:
                self.delete_created_branch(name=branch)

        super(BranchTests, self).tearDown()

    def test001_create_new_branch(self):
        """ Branch-1: Test case for check create new branch.*

        **Test Scenario:**

        #. do create branch with valid, should succeed
        #. check new branch created successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        self.lg('%s ENDED' % self._testID)

    def test002_validate_create_new_branch_parameters(self):
        """ Branch-2: Test case for validate create new branch parameters.*

        **Test Scenario:**

        #. click create new branch, should succeed
        #. validate create new branch requirements, should succeed
        #. do create branch with one character, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. do create branch with invaild characters, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. do create branch with invaild max length, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. do create branch with valid, should succeed
        #. click cancel branch, should succeed
        #. check new branch not created, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('click create new branch, should succeed')
        self.click_create_new_branch()
        self.lg('validate create new branch requirements, should succeed')
        self.assertTrue(self.element_is_readonly('new_branch_id'))
        self.assertTrue(self.element_is_enabled('new_branch_name'))
        self.assertTrue(self.element_is_displayed('new_branch_name_req'))
        self.assertTrue(self.element_is_enabled('new_branch_code'))
        self.assertTrue(self.element_is_displayed('new_branch_code_req'))
        self.lg('do create branch with one character, should succeed')
        self.create_new_branch(name='a', code='1')
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_req'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid_length'))
        self.assertFalse(self.element_is_displayed('new_branch_code_req'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid_length'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid_length'),
                         'This field is required to be at least 5 characters.')
        self.assertEqual(self.get_text('new_branch_code_invalid_length'),
                         'This field is required to be at least 2 characters.')
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('do create branch with invaild characters, should succeed')
        self.create_new_branch(name='12345', code='ab')
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_invalid_length'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid'))
        self.assertFalse(self.element_is_displayed('new_branch_code_invalid_length'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid'))
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid'),
                         'This field should follow pattern ^[a-zA-Z\s]*$.')
        self.assertEqual(self.get_text('new_branch_code_invalid'),
                         'This field should follow pattern ^[A-Z0-9]*$.')
        self.lg('do create branch with invaild max length, should succeed')
        self.create_new_branch(name='a'*21, code='1'*11)
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_invalid'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid_maxlength'))
        self.assertFalse(self.element_is_displayed('new_branch_code_invalid'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid_maxlength'))
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid_maxlength'),
                         'This field cannot be longer than 20 characters.')
        self.assertEqual(self.get_text('new_branch_code_invalid_maxlength'),
                         'This field cannot be longer than 10 characters.')
        self.lg('do create branch with vaild, should succeed')
        self.create_new_branch()
        self.lg('click cancel branch, should succeed')
        self.click_cancel_branch()
        self.lg('check new branch not created, should succeed')
        self.assertFalse(self.search_branch(self.name, self.code))
        self.lg('%s ENDED' % self._testID)

    def test003_view_delete_branch(self):
        """ Branch-3: Test case for check view/delete branch.*

        **Test Scenario:**

        #. do create branch with valid, should succeed
        #. check new branch created successfully, should succeed
        #. view branch with valid, should succeed
        #. check new branch updated successfully, should succeed
        #. delete branch, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        self.lg('view branch with name, should succeed')
        self.assertTrue(self.view_branch(self.name, self.code))
        self.assertTrue(self.element_is_readonly('search_branch_view_name'))
        self.assertTrue(self.element_is_readonly('search_branch_view_code'))
        self.assertEqual(self.get_value('search_branch_view_name'), self.name)
        self.assertEqual(self.get_value('search_branch_view_code'), self.code)
        self.click_view_back()
        self.lg('delete branch, should succeed')
        self.delete_created_branch(name=self.name)
        self.assertFalse(self.search_branch(self.name, self.code))
        self.lg('%s ENDED' % self._testID)

    def test004_edit_delete_branch(self):
        """ Branch-4: Test case for check edit/delete created branch.*

        **Test Scenario:**

        #. do create branch with valid, should succeed
        #. check new branch created successfully, should succeed
        #. edit branch with valid, should succeed
        #. check new branch updated successfully, should succeed
        #. delete branch, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        self.lg('edit branch with valid, should succeed')
        self.edit_branch(self.name, self.code)
        self.edit_created_branch()
        self.click_save_edit_branch()
        self.lg('check new branch updated successfully, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        self.lg('delete branch, should succeed')
        self.delete_created_branch(name=self.name)
        self.assertFalse(self.search_branch(self.name, self.code))
        self.lg('%s ENDED' % self._testID)

    def test005_validate_edit_branch_parameters(self):
        """ Branch-5: Test case for validate create edit branch parameters.*

        **Test Scenario:**

        #. click create new branch, should succeed
        #. validate create new branch requirements, should succeed
        #. edit branch with one character, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. edit branch with invaild characters, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. edit branch with invaild max length, should succeed
        #. validate create new branch requirements, should succeed
        #. proper error message, should succeed
        #. do create branch with valid, should succeed
        #. click cancel edit branch, should succeed
        #. check created branch not updated, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create branch with valid, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('check new branch created successfully, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        start_name = self.name
        start_code = self.code
        self.edit_branch(self.name, self.code)
        self.lg('validate create new branch requirements, should succeed')
        self.set_text('edit_branch_name', '')
        self.set_text('new_branch_code', '')
        self.assertTrue(self.element_is_readonly('new_branch_id'))
        self.assertTrue(self.element_is_enabled('new_branch_name'))
        self.assertTrue(self.element_is_displayed('new_branch_name_req'))
        self.assertTrue(self.element_is_enabled('new_branch_code'))
        self.assertTrue(self.element_is_displayed('new_branch_code_req'))

        self.lg('edit branch with one character, should succeed')
        self.edit_created_branch(name='a', code='1')
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_req'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid_length'))
        self.assertFalse(self.element_is_displayed('new_branch_code_req'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid_length'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid_length'),
                         'This field is required to be at least 5 characters.')
        self.assertEqual(self.get_text('new_branch_code_invalid_length'),
                         'This field is required to be at least 2 characters.')
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('edit branch with invaild characters, should succeed')
        self.edit_created_branch(name='12345', code='ab')
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_invalid_length'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid'))
        self.assertFalse(self.element_is_displayed('new_branch_code_invalid_length'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid'))
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid'),
                         'This field should follow pattern ^[a-zA-Z\s]*$.')
        self.assertEqual(self.get_text('new_branch_code_invalid'),
                         'This field should follow pattern ^[A-Z0-9]*$.')
        self.lg('edit branch with invaild max length, should succeed')
        self.edit_created_branch(name='a'*21, code='1'*11)
        self.lg('validate create new branch parameters, should succeed')
        self.assertFalse(self.element_is_displayed('new_branch_name_invalid'))
        self.assertTrue(self.element_is_displayed('new_branch_name_invalid_maxlength'))
        self.assertFalse(self.element_is_displayed('new_branch_code_invalid'))
        self.assertTrue(self.element_is_displayed('new_branch_code_invalid_maxlength'))
        self.assertFalse(self.element_is_enabled('save_branch_button'))
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('new_branch_name_invalid_maxlength'),
                         'This field cannot be longer than 20 characters.')
        self.assertEqual(self.get_text('new_branch_code_invalid_maxlength'),
                         'This field cannot be longer than 10 characters.')
        self.lg('edit branch with vaild, should succeed')
        self.edit_created_branch()
        self.lg('click cancel branch, should succeed')
        self.click_cancel_edit_branch()
        self.lg('check new branch not updated, should succeed')
        self.assertFalse(self.search_branch(self.name, self.code))
        self.assertTrue(self.search_branch(start_name, start_code))
        self.lg('%s ENDED' % self._testID)

    def test006_validate_search_delete_branch(self):
        """ Branch-6: Test case for validate search/delete branch.*

        **Test Scenario:**

        #. do create new branch, should succeed
        #. search new branch, should succeed
        #. delete branch, should succeed
        #. search new branch, should fail
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new branch, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('search new branch, should succeed')
        self.assertTrue(self.search_branch(self.name, self.code))
        self.lg('delete branch, should succeed')
        self.delete_created_branch(name=self.name)
        self.lg('search new branch, should fail')
        self.assertFalse(self.search_branch(self.name, self.code))
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal name', str(uuid.uuid4())),
                           ('long name', 'X'*1000),
                           ('numeric name', 9876543210),
                           ('special chars name', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test007_validate_search_delete_invalid_branch(self, _, name):
        """ Branch-7: Test case for validate search/delete invalid branch.*

        **Test Scenario:**

        #. do create new branch, should succeed
        #. search invalid branch, should fail
        #. delete branch, should succeed
        #. search invalid branch, should fail
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new branch, should succeed')
        self.click_create_new_branch()
        self.create_new_branch()
        self.click_save_branch()
        self.lg('search invalid branch, should fail')
        self.assertFalse(self.search_branch(name, self.code))
        self.lg('delete branch, should succeed')
        self.delete_created_branch(name=self.name)
        self.lg('search invalid branch, should fail')
        self.assertFalse(self.search_branch(name, self.code))
        self.lg('%s ENDED' % self._testID)

    def test008_validate_search_different_branch(self):
        """ Branch-8: Test case for validate search different branch.

        **Test Scenario:**

        #. do create new branch1, should succeed
        #. search new branch1, should succeed
        #. do create new branch2, should succeed
        #. search new branch2, should succeed
        #. search new branch1, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do create new branch1, should succeed')
        branch_1 = 'brancha'
        for _ in range(2):
            self.click_create_new_branch()
            self.create_new_branch(name=branch_1)
            self.click_save_branch()
            self.lg('check new branch created successfully, should succeed')
            self.assertTrue(self.search_branch(branch_1, self.code))

        self.lg('search new branch1, should succeed')
        self.search_branch(branch_1, self.code)
        self.assertEqual(self.get_table_count(), 2)
        self.lg('do create new branch1, should succeed')
        branch_2 = 'branchb'
        for _ in range(3):
            self.click_create_new_branch()
            self.create_new_branch(name=branch_2)
            self.click_save_branch()
            self.lg('check new branch created successfully, should succeed')
            self.assertTrue(self.search_branch(branch_2, self.code))

        self.lg('search new branch1, should succeed')
        self.search_branch(branch_2, self.code)
        self.assertEqual(self.get_table_count(), 3)
        self.lg('search new branch1, should succeed')
        self.search_branch(branch_1, self.code)
        self.assertEqual(self.get_table_count(), 2)
        self.lg('%s ENDED' % self._testID)

