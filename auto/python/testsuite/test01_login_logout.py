from testframework.base import *
import uuid
from nose_parameterized import parameterized


class LoginLogoutTests(BaseTest):


    def setUp(self):
        super(LoginLogoutTests, self).setUp()
        self.go_to_login_page()

    def test001_login(self):
        """ Login-Logout-1
        *Test case for check user potal login.*

        **Test Scenario:**

        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using admin username/password, should succeed')
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('%s ENDED' % self._testID)

    def test002_logout(self):
        """ Login-Logout-2
        *Test case for check user potal logout.*

        **Test Scenario:**

        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        #. do logout, should succeed
        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using admin username/password, should succeed')
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('do logout, should succeed')
        self.logout()
        self.assertEqual(self.get_text('login_text'), 'Click here to login')
        self.lg('do login using admin username/password again, should succeed')
        self.go_to_login_page()
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal username', str(uuid.uuid4())),
                           ('empty username', ''),
                           ('long username', 'X'*1000),
                           ('numeric username', 9876543210),
                           ('special chars username', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test003_login_wrong_username(self, _, username):
        """ Login-Logout-3
        *Test case for check user potal login with wrong username.*

        **Test Scenario:**

        #. do login using wrong username, should fail
        #. proper error message, should succeed
        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        #. do logout, should succeed

        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using wrong username, should succeed')
        self.login(username=username)
        self.assertEqual(self.get_text('authentication_error'),
                         'Authentication failed! Please check your credentials and try again.')
        self.lg('do login using admin username/password, should succeed')
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('do logout, should succeed')
        self.logout()
        self.assertEqual(self.get_text('login_text'), 'Click here to login')
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal password', str(uuid.uuid4())),
                           ('empty password', ''),
                           ('long password', 'X'*1000),
                           ('numeric password', 9876543210),
                           ('special chars password', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test004_login_wrong_password(self, _, password):
        """ Login-Logout-4
        *Test case for check user potal login with wrong password.*

        **Test Scenario:**

        #. check the login page title, should succeed
        #. do login using wrong password, should fail
        #. proper error message, should succeed
        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        #. do logout, should succeed
        #. check the login page title, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using wrong password, should succeed')
        self.login(password=password)
        self.assertEqual(self.get_text('authentication_error'),
                         'Authentication failed! Please check your credentials and try again.')
        self.lg('do login using admin username/password, should succeed')
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('do logout, should succeed')
        self.logout()
        self.assertEqual(self.get_text('login_text'), 'Click here to login')
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal username/password', str(uuid.uuid4())),
                           ('empty username/password', ''),
                           ('long username/password', 'X'*1000),
                           ('numeric username/password', 9876543210),
                           ('special chars username/password', '+_=-)(*&^#@!~`{}[];\',.<>\/')])
    def test005_login_wrong_username_password(self, _, name):
        """ Login-Logout-5
        *Test case for check user potal login with wrong username/password.*

        **Test Scenario:**

        #. check the login page title, should succeed
        #. do login using wrong username/password, should fail
        #. proper error message, should succeed
        #. do login using admin username/password, should succeed
        #. check the login successfully, should succeed
        #. do logout, should succeed
        #. check the login page title, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using wrong username/password, should succeed')
        self.login(username=name, password=name)
        self.assertEqual(self.get_text('authentication_error'),
                         'Authentication failed! Please check your credentials and try again.')
        self.lg('do login using admin username/password, should succeed')
        self.login()
        self.lg('check the login successfully, should succeed')
        self.assertEqual(self.get_text('logged'),
                         'You are logged in as user "%s".' % self.admin_username)
        self.lg('do logout, should succeed')
        self.logout()
        self.assertEqual(self.get_text('login_text'), 'Click here to login')
        self.lg('%s ENDED' % self._testID)
