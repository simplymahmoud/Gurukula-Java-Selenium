from testframework.base import *
import uuid
from nose_parameterized import parameterized


class AccountTests(BaseTest):

    def setUp(self):
        super(AccountTests, self).setUp()
        self.go_to_login_page()
        self.login()
        self.go_to_account_menu()

    def test001_view_save_account_settings(self):
        """ Account-1: Test case for check view/save account settings.*

        **Test Scenario:**

        #. go to account settings page, should succeed
        #. view/fill all fields with proper values, should succeed
        #. check save settings successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('do login using admin username/password, should succeed')
        self.go_to_account_settings()
        self.lg('view/fill all fields with proper values, should succeed')
        self.fill_settings()
        self.assertTrue(self.element_is_enabled('settings_save_button'))
        self.lg('check save settings successfully, should succeed')
        self.click_account_settings_save()
        self.assertEqual(self.get_text('settings_saved'),
                         'Settings saved!')
        self.lg('%s ENDED' % self._testID)

    def test002_save_account_settings_invalid_short_email(self):
        """ Account-2: Test case for check save account settings with invalid/short email.*

        **Test Scenario:**

        #. fill email filed with invalid/short value, should succeed
        #. proper error message, should succeed
        #. fill email filed with invalid value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check save account settings successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill email filed with invalid/short value, should succeed')
        self.go_to_account_settings()
        self.fill_settings(email='ss')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('settings_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertEqual(self.get_text('settings_invalidmaillenght'),
                         'Your e-mail is required to be at least 5 characters.')
        self.assertFalse(self.element_is_enabled('settings_save_button'))
        self.lg('fill email filed with invalid value, should succeed')
        self.fill_settings(email='ss2ss.s')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('settings_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertFalse(self.element_is_displayed('settings_invalidmaillenght'))
        self.assertFalse(self.element_is_enabled('settings_save_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_settings()
        self.assertTrue(self.element_is_enabled('settings_save_button'))
        self.assertFalse(self.element_is_displayed('settings_invalidmail'))
        self.assertFalse(self.element_is_displayed('settings_invalidmaillenght'))
        self.lg('check save settings successfully, should succeed')
        self.click_account_settings_save()
        self.assertEqual(self.get_text('settings_saved'),
                         'Settings saved!')
        self.lg('%s ENDED' % self._testID)

    @parameterized.expand([('normal email', str(uuid.uuid4())),
                           ('long email', 'X'*1000),
                           ('numeric email', 9876543210),
                           ('special chars email', '+_=-)(*&^#!~`{}[];\',.<>\/')])
    def test003_save_account_settings_invalid_email(self, _, email):
        """ Account-3: Test case for check save account settings with invalid email.*

        **Test Scenario:**

        #. fill email filed with invalid value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check save account settings successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill email filed with invalid value, should succeed')
        self.go_to_account_settings()
        self.fill_settings(email=email)
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('settings_invalidmail'),
                         'Your e-mail is invalid.')
        self.assertFalse(self.element_is_displayed('settings_invalidmaillenght'))
        self.assertFalse(self.element_is_enabled('settings_save_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_settings()
        self.assertTrue(self.element_is_enabled('settings_save_button'))
        self.assertFalse(self.element_is_displayed('settings_invalidmail'))
        self.assertFalse(self.element_is_displayed('settings_invalidmaillenght'))
        self.lg('check save settings successfully, should succeed')
        self.click_account_settings_save()
        self.assertEqual(self.get_text('settings_saved'),
                         'Settings saved!')
        self.lg('%s ENDED' % self._testID)

    def test004_save_account_settings_required_fileds(self):
        """ Account-4: Test case for check save account settings with empty fields.*

        **Test Scenario:**

        #. fill all fields with empty values, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check save settings successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with empty value, should succeed')
        self.go_to_account_settings()
        self.fill_settings()
        self.fill_settings(firstname='', lastname='', email='')
        self.assertEqual(self.get_text('settings_firstnamereq'),
                         'Your first name is required.')
        self.assertEqual(self.get_text('settings_lastnamereq'),
                         'Your last name is required.')
        self.assertEqual(self.get_text('settings_mailreq'),
                         'Your e-mail is required.')
        self.assertFalse(self.element_is_enabled('settings_save_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_settings()
        self.assertTrue(self.element_is_enabled('settings_save_button'))
        self.assertFalse(self.element_is_displayed('settings_firstnamereq'))
        self.assertFalse(self.element_is_displayed('settings_lastnamereq'))
        self.lg('check save settings successfully, should succeed')
        self.click_account_settings_save()
        self.assertEqual(self.get_text('settings_saved'),
                         'Settings saved!')
        self.lg('%s ENDED' % self._testID)

    def test005_save_account_passwords_invalid_password(self):
        """ Account-5: Test case for check save account passwords with invalid password.*

        **Test Scenario:**

        #. fill password filed with invalid/short value, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check save password successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with invalid/short value, should succeed')
        self.go_to_account_passwords()
        self.fill_passwords(newpasswd='ss', passwdcfm='ss')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('passwords_invalidpasswdlenght'),
                         'Your password is required to be at least 5 characters.')
        self.assertEqual(self.get_text('passwords_invalidpasswdcnflenght'),
                         'Your confirmation password is required to be at least 5 characters.')
        self.assertFalse(self.element_is_enabled('passwords_save_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_passwords()
        self.assertTrue(self.element_is_enabled('passwords_save_button'))
        self.assertFalse(self.element_is_displayed('passwords_invalidpasswdlenght'))
        self.assertFalse(self.element_is_displayed('passwords_invalidpasswdcnflenght'))
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        #Currently save password is not available
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('%s ENDED' % self._testID)

    def test006_save_account_passwords_required_fileds(self):
        """ Account-6: Test case for check save account passwords with empty fields.*

        **Test Scenario:**

        #. fill all fields with empty values, should succeed
        #. proper error message, should succeed
        #. fill input fields with valid parameters, should succeed
        #. check save password successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with empty value, should succeed')
        self.go_to_account_passwords()
        self.fill_passwords()
        self.fill_passwords(newpasswd='', passwdcfm='')
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('passwords_passwdreq'),
                         'Your password is required.')
        self.assertEqual(self.get_text('passwords_passwdcnfreq'),
                         'Your confirmation password is required.')
        self.assertFalse(self.element_is_enabled('passwords_save_button'))
        self.lg('fill input fields with valid parameters, should succeed')
        self.fill_passwords()
        self.assertTrue(self.element_is_enabled('passwords_save_button'))
        self.assertFalse(self.element_is_displayed('passwords_passwdreq'))
        self.assertFalse(self.element_is_displayed('passwords_passwdcnfreq'))
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('%s ENDED' % self._testID)

    def test007_save_account_passwords_password_strength(self):
        """ Account-7: Test case for check register new user check password strength.*

        **Test Scenario:**

        #. fill password filed with numbers value, should succeed
        #. check save password successfully, should succeed
        #. fill password filed with numbers/letters value, should succeed
        #. check save password successfully, should succeed
        #. fill password filed with numbers/small/capital letters value, should succeed
        #. check save password successfully, should succeed
        #. fill password filed with numbers/small/capital/special value, should succeed
        #. check save password successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with numbers value, should succeed')
        self.go_to_account_passwords()
        password = '12345'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(255, 0, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(221, 221, 221, 1)')
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('fill password filed with numbers/letters value, should succeed')
        password = '12345abcde'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
        self.assertEqual(self.element_background_color('registration_passbar1'),
                         'rgba(255, 153, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar2'),
                         'rgba(255, 153, 0, 1)')
        self.assertEqual(self.element_background_color('registration_passbar3'),
                         'rgba(221, 221, 221, 1)')
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('fill password filed with numbers/small/capital letters value, should succeed')
        password = '12345abcdeABC'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
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
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('fill password filed with numbers/small/capital/special value, should succeed')
        password = '12345abcdeABC!'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
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
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('%s ENDED' % self._testID)

    def test008_save_account_passwords_password_max_length(self):
        """ Account-8: Test case for check save account passwords with password max length.*

        **Test Scenario:**

        #. fill password filed with invalid/long value, should succeed
        #. proper error message, should succeed
        #. fill password filed with valid value, should succeed
        #. check save password successfully, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password filed with invalid/long value, should succeed')
        self.go_to_account_passwords()
        password = 51 * 'x'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
        self.lg('proper error message, should succeed')
        self.assertFalse(self.element_is_enabled('passwords_save_button'))
        self.assertEqual(self.get_text('passwords_maxpasswdlenght'),
                         'Your password cannot be longer than 50 characters.')
        self.lg('fill password filed with valid value, should succeed')
        password = 50 * 'x'
        self.fill_passwords(newpasswd=password, passwdcfm=password)
        self.assertTrue(self.element_is_enabled('passwords_save_button'))
        self.assertFalse(self.element_is_displayed('passwords_maxpasswdlenght'))
        self.click_account_password_save()
        self.lg('check save password successfully, should succeed')
        self.assertEqual(self.get_text('passwords_notsaved'),
                         'An error has occurred!')
        self.lg('%s ENDED' % self._testID)

    def test009_save_account_passwords_password_not_match(self):
        """ Account-9: Test case for check save account passwords with password not match.*

        **Test Scenario:**

        #. fill password/confirmed filed with different value, should succeed
        #. proper error message, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('fill password/confirmed filed with different value, should succeed')
        self.go_to_account_passwords()
        self.fill_passwords(newpasswd='sssss', passwdcfm='SSSSS')
        self.assertTrue(self.element_is_enabled('passwords_save_button'))
        self.click_account_password_save()
        self.lg('proper error message, should succeed')
        self.assertEqual(self.get_text('passwords_passmissmatch'),
                         'The password and its confirmation do not match!')
        self.lg('%s ENDED' % self._testID)

    def test010_account_sessions(self):
        """ Account-10: Test case for check account sessions.*

        **Test Scenario:**

        #. click invalidate session, should succeed
        #. sessions table should be reduced by one, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        self.lg('click invalidate session, should succeed')
        self.click('account_session')
        first_count = self.get_table_count('account_session_table')
        if first_count:
            self.invalidate_session()
            self.lg('sessions table should be reduced by one, should succeed')
            self.assertEqual(self.get_text('account_session_invalidate'),
                             'Session invalidated!')
            last_count = self.get_table_count('account_session_table')
            self.assertEqual(first_count, last_count + 1)

        self.lg('%s ENDED' % self._testID)