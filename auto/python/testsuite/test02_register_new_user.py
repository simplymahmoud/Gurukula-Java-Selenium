from testframework.base import *
import uuid
from nose_parameterized import parameterized


class RegisterNewUserTests(BaseTest):


    def setUp(self):
        super(RegisterNewUserTests, self).setUp()
        self.go_to_register_new_user_page()

    def test001_register_new_user(self):
        """ Register-New-User-1: Test case for check register new user.*

        **Test Scenario:**

        #. fill input fields with valid parameters, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_register_new_user()
        self.assertTrue(self.element_is_enabled('register_button'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test002_register_new_user_invalid_email_length_format(self):
        """ Register-New-User-2: Test case for check register new user with invalid email.*

        **Test Scenario:**

        #. fill email filed with invalid/short value, should succeed
        #. proper error message, should succeed
        #. fill email filed with invalid value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill email filed with invalid/short value, should succeed')
        self.fill_register_new_user(email='ss')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertEqual(self.get_text('registration_invalidmaillenght'),
                         'Your e-mail is required to be at least 5 characters.')
        self.assertFalse(self.element_is_enabled('register_button'))
        self.lg('fill email filed with invalid value, should succeed')
        self.fill_register_new_user(email='ss2ss.s')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertFalse(self.element_is_displayed('registration_invalidmaillenght'))
        self.assertFalse(self.element_is_enabled('register_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_register_new_user()
        self.assertTrue(self.element_is_enabled('register_button'))
        self.assertFalse(self.element_is_displayed('registration_invalidmail'))
        self.assertFalse(self.element_is_displayed('registration_invalidmaillenght'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal email', str(uuid.uuid4())),
                           ('long email', 'X'*1000),
                           ('numeric email', 9876543210),
                           ('special chars email', '+_=-)(*&^#!~`{}[];\',.<>\/')])
    def test003_register_new_user_invalid_email(self, _, email):
        """ Register-New-User-3: Test case for check register new user with invalid email.*

        **Test Scenario:**

        #. fill email filed with invalid value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill email filed with invalid value, should succeed')
        self.fill_register_new_user(email=email)
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertFalse(self.element_is_displayed('registration_invalidmaillenght'))
        self.assertFalse(self.element_is_enabled('register_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_register_new_user()
        self.assertTrue(self.element_is_enabled('register_button'))
        self.assertFalse(self.element_is_displayed('registration_invalidmail'))
        self.assertFalse(self.element_is_displayed('registration_invalidmaillenght'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test004_register_new_user_invalid_password(self):
        """ Register-New-User-4: Test case for check register new user with invalid password.*

        **Test Scenario:**

        #. fill password filed with invalid/short value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with invalid/short value, should succeed')
        self.fill_register_new_user(newpasswd='ss', passwdcfm='ss')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_invalidpasswdlenght'),
                         'Your password is required to be at least 5 characters.')
        self.assertEqual(self.get_text('registration_invalidcnfpasswdlenght'),
                         'Your confirmation password is required to be at least 5 characters.')
        self.assertFalse(self.element_is_enabled('register_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_register_new_user()
        self.assertTrue(self.element_is_enabled('register_button'))
        self.assertFalse(self.element_is_displayed('registration_invalidpasswdlenght'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test005_register_new_user_required_fileds(self):
        """ Register-New-User-5: Test case for check register new user with empty fields.*

        **Test Scenario:**

        #. fill all fields with empty values, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill all fields with empty values, should succeed')
        self.fill_register_new_user()
        self.fill_register_new_user(login='', email='', newpasswd='', passwdcfm='')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_loginreq'),
                         'Your login is required.')
        self.assertEqual(self.get_text('registration_mailreq'),
                         'Your e-mail is required.')
        self.assertEqual(self.get_text('registration_passwdreq'),
                         'Your password is required.')
        self.assertEqual(self.get_text('registration_cnfpasswdreq'),
                         'Your confirmation password is required.')
        self.assertFalse(self.element_is_enabled('register_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_register_new_user()
        self.assertTrue(self.element_is_enabled('register_button'))
        self.assertFalse(self.element_is_displayed('registration_loginreq'))
        self.assertFalse(self.element_is_displayed('registration_mailreq'))
        self.assertFalse(self.element_is_displayed('registration_passwdreq'))
        self.assertFalse(self.element_is_displayed('registration_cnfpasswdreq'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test006_register_new_user_password_strength(self):
        """ Register-New-User-6: Test case for check register new user check password strength.*

        **Test Scenario:**

        #. fill password filed with numbers value, should succeed
        #. check registeration successfully, should succeed
        #. fill password filed with numbers/letters value, should succeed
        #. check registeration successfully, should succeed
        #. fill password filed with numbers/small/capital letters value, should succeed
        #. check registeration successfully, should succeed
        #. fill password filed with numbers/small/capital/special value, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with numbers value, should succeed')
        password = '12345'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(255, 0, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(221, 221, 221, 1)')
        self.assertTrue(self.element_is_enabled('register_button'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('fill password filed with numbers/letters value, should succeed')
        password = '12345abcde'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(255, 153, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(255, 153, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar3'),
                         'rgba(221, 221, 221, 1)')
        self.assertTrue(self.element_is_enabled('register_button'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('fill password filed with numbers/small/capital letters value, should succeed')
        password = '12345abcdeABC'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(153, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(153, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar3'),
                         'rgba(153, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar4'),
                         'rgba(153, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar5'),
                         'rgba(221, 221, 221, 1)')
        self.assertTrue(self.element_is_enabled('register_button'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('fill password filed with numbers/small/capital/special value, should succeed')
        password = '12345abcdeABC!'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(0, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(0, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar3'),
                         'rgba(0, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar4'),
                         'rgba(0, 255, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar5'),
                         'rgba(0, 255, 0, 1)')
        self.assertTrue(self.element_is_enabled('register_button'))
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test007_register_new_user_password_max_length(self):
        """ Register-New-User-7: Test case for check register new user with password max length.*

        **Test Scenario:**

        #. fill password filed with invalid/long value, should succeed
        #. proper error message, should succeed
        #. fill password filed with valid value, should succeed
        #. check registeration successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with invalid/long value, should succeed')
        password = 51 * 'x'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_maxpasswdlenght'),
                         'Your password cannot be longer than 50 characters.')
        self.lg('fill password filed with valid value, should succeed')
        password = 50 * 'x'
        self.fill_register_new_user(newpasswd=password, passwdcfm=password)
        self.register_new_user()
        self.lg('check registeration successfully, should succeed')
        #Currently registration is unavailable, so will expect that as success
        self.assertEqual(self.get_text('registration_error'),
                         'Registration failed! Please try again later.')
        self.lg('%s ENDED' % self._testID)

    def test008_register_new_user_password_not_match(self):
        """ Register-New-User-8: Test case for check register new user with password not match.*

        **Test Scenario:**

        #. fill password/confirmed filed with different value, should succeed
        #. proper error message, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password/confirmed filed with different value, should succeed')
        self.fill_register_new_user(newpasswd='sssss', passwdcfm='SSSSS')
        self.register_new_user()
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('registration_passmissmatch'),
                         'The password and its confirmation do not match!')
        self.lg('%s ENDED' % self._testID)
