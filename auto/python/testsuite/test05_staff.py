from testframework.base import *
import time


class StaffTests(BaseTest):

    def setUp(self):
        super(StaffTests, self).setUp()
        self.go_to_login_page()
        self.login()
        time.sleep(1)
        self.click('entities_menu')
        self.click('entities_staff')

    def test001_staff(self):
        """ Staff-1
        *Test case for check user potal login.*

        **Test Scenario:**

        #. do login using username/password, should succeed
        #. check the login successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using username/password, should succeed')

        self.lg('check the login successfully, should succeed')

        self.lg('%s ENDED' % self._testID)