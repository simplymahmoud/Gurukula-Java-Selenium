package testsuite;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

import framework.factory;
import framework.model.AccountPage;


public class Account extends factory{

	@Before
	public void test_setup() throws Exception {
		click_login();
		fill_login("admin", "admin");
		click_authenticat();
		click_account_menu();
	}
	
	@Test
	public void Account_1() throws Exception {
		//('view/fill all fields with proper values, should succeed')
		click_account_settings();
		fill_settings("Administrator", "Administrator", "admin@localhost");
		boolean register_btn = element_is_enabled(AccountPage.settings_save_button);
		assertTrue(register_btn);
		//('check save settings successfully, should succeed')
		click_btn(AccountPage.settings_save_button);
		String logged_text = get_text_filed(AccountPage.settings_saved);
		String expected_text = "Settings saved!";
		assertEquals(logged_text, expected_text);		
	}
	
	@Test
	public void Account_2() throws Exception {
		//('fill email filed with invalid/short value, should succeed')
		click_account_settings();
		String email = generate_string(2);
		fill_settings("Administrator", "Administrator", email);
		//('proper error message, should succeed')
		String logged_text = get_text_filed(AccountPage.settings_invalidmail);
		String expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(AccountPage.settings_invalidmaillenght);
		expected_text = "Your e-mail is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		boolean save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertFalse(save_btn);
		//('fill email filed with invalid value, should succeed')
		email = generate_string(5);
		fill_settings("Administrator", "Administrator", email);
		//('proper error message, should succeed')
		logged_text = get_text_filed(AccountPage.settings_invalidmail);
		expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);
		boolean invalid_txt = element_is_displayed(AccountPage.settings_invalidmaillenght);
		assertFalse(invalid_txt);
		save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
		fill_settings("Administrator", "Administrator", "admin@localhost");
		invalid_txt = element_is_displayed(AccountPage.settings_invalidmaillenght);
		assertFalse(invalid_txt);
		save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertTrue(save_btn);
		click_btn(AccountPage.settings_save_button);
		//('check save settings successfully, should succeed')
		//but its non issue its not saved
		logged_text = get_text_filed(AccountPage.settings_saved);
		expected_text = "Settings saved!";
		assertEquals(logged_text, expected_text);	
	}	
	
	@Test
	public void Account_3() throws Exception {
		//('fill email filed with invalid value, should succeed')
		click_account_settings();
		fill_settings("Administrator", "Administrator", "+_=-)(*&^#!~`{}[];',.<>/");
		//('proper error message, should succeed')		
		String logged_text = get_text_filed(AccountPage.settings_invalidmail);
		String expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);
		boolean invalid_txt = element_is_displayed(AccountPage.settings_invalidmaillenght);
		assertFalse(invalid_txt);	
		boolean save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
		fill_settings("Administrator", "Administrator", "admin@localhost");
		invalid_txt = element_is_displayed(AccountPage.settings_invalidmail);
		assertFalse(invalid_txt);
		save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertTrue(save_btn);
		click_btn(AccountPage.settings_save_button);
		//('check save settings successfully, should succeed')
		//but its non issue its not saved		
		logged_text = get_text_filed(AccountPage.settings_saved);
		expected_text = "Settings saved!";
		assertEquals(logged_text, expected_text);
	}	
	
	@Test
	public void Account_4() throws Exception {
		//('fill password filed with empty value, should succeed')
	    click_account_settings();
	    fill_settings("Administrator", "Administrator", "admin@localhost");
	    fill_settings("", "", "");
		//('proper error message, should succeed')
		String logged_text = get_text_filed(AccountPage.settings_firstnamereq);
		String expected_text = "Your first name is required.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(AccountPage.settings_lastnamereq);
		expected_text = "Your last name is required.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(AccountPage.settings_mailreq);
		expected_text = "Your e-mail is required.";
		assertEquals(logged_text, expected_text);
		boolean save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
		fill_settings("Administrator", "Administrator", "admin@localhost");
		boolean invalid_txt = element_is_displayed(AccountPage.settings_firstnamereq);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(AccountPage.settings_lastnamereq);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(AccountPage.settings_mailreq);
		assertFalse(invalid_txt);		
		save_btn = element_is_enabled(AccountPage.settings_save_button);
		assertTrue(save_btn);
		click_btn(AccountPage.settings_save_button);
		//('check save settings successfully, should succeed')
		//but its non issue its not saved
		logged_text = get_text_filed(AccountPage.settings_saved);
		expected_text = "Settings saved!";
		assertEquals(logged_text, expected_text);
	}		
	
	
	@Test
	public void Account_5() throws Exception {
		//('fill password filed with invalid/short value, should succeed')
	    click_account_passwords();
	    String password = generate_string(2);
	    fill_passwords(password, password);
		//('proper error message, should succeed')
	    String logged_text = get_text_filed(AccountPage.passwords_invalidpasswdlenght);
	    String expected_text = "Your password is required to be at least 5 characters.";
	    assertEquals(logged_text, expected_text);
	    logged_text = get_text_filed(AccountPage.passwords_invalidpasswdcnflenght);
	    expected_text = "Your confirmation password is required to be at least 5 characters.";
	    assertEquals(logged_text, expected_text);
	    boolean save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
	    password = generate_string(5);
	    fill_passwords(password, password);
	    boolean invalid_txt = element_is_displayed(AccountPage.passwords_invalidpasswdlenght);
	    assertFalse(invalid_txt);
	    invalid_txt = element_is_displayed(AccountPage.passwords_invalidpasswdcnflenght);
	    assertFalse(invalid_txt);	        
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);
	    click_btn(AccountPage.passwords_save_button);
		//('check save settings successfully, should succeed')
		//but its non issue its not saved
	    logged_text = get_text_filed(AccountPage.passwords_notsaved);
	    expected_text = "An error has occurred!";
	    assertEquals(logged_text, expected_text);
	}	
	
	@Test
	public void Account_6() throws Exception {
		//('fill password filed with empty value, should succeed')
		click_account_passwords();
	    String password = generate_string(5);
	    fill_passwords(password, password);
	    fill_passwords("", "");
		//('proper error message, should succeed')
		String logged_text = get_text_filed(AccountPage.passwords_passwdreq);
		String expected_text = "Your password is required.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(AccountPage.passwords_passwdcnfreq);
		expected_text = "Your confirmation password is required.";
		assertEquals(logged_text, expected_text);
		boolean save_btn = element_is_enabled(AccountPage.passwords_save_button);
		assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
	    fill_passwords(password, password);
	    boolean invalid_txt = element_is_displayed(AccountPage.passwords_passwdreq);
	    assertFalse(invalid_txt);
	    invalid_txt = element_is_displayed(AccountPage.passwords_passwdcnfreq);
	    assertFalse(invalid_txt);	        
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);
	    click_btn(AccountPage.passwords_save_button);
		//('check save passwords successfully, should succeed')
		//but its non issue its not saved
	    logged_text = get_text_filed(AccountPage.passwords_notsaved);
	    expected_text = "An error has occurred!";
	    assertEquals(logged_text, expected_text);
	}		
	
	
	@Test
	public void Account_7() throws Exception {
		//('fill password filed with numbers value, should succeed')
		click_account_passwords();
		fill_passwords("12345", "12345");
		String bar_color = element_background_color(AccountPage.passwords_passbar1);
		String expected_color = "rgba(255, 0, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(AccountPage.passwords_passbar2);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar3);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar4);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
		boolean save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);
		//('fill password filed with numbers/letters value, should succeed')
	    fill_passwords("12345abcde", "12345abcde");
		bar_color = element_background_color(AccountPage.passwords_passbar1);
		expected_color = "rgba(255, 153, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(AccountPage.passwords_passbar2);
		expected_color = "rgba(255, 153, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar3);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar4);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);
		//('fill password filed with numbers/small/capital letters value, should succeed')
	    fill_passwords("12345abcdeABC", "12345abcdeABC");
		bar_color = element_background_color(AccountPage.passwords_passbar1);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(AccountPage.passwords_passbar2);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar3);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar4);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);		
	    //('fill password filed with numbers/small/capital/special value, should succeed')
	    fill_passwords("12345abcdeABC!", "12345abcdeABC!");
		bar_color = element_background_color(AccountPage.passwords_passbar1);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(AccountPage.passwords_passbar2);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar3);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar4);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(AccountPage.passwords_passbar5);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);	
	    click_btn(AccountPage.passwords_save_button);
		//('check save passwords successfully, should succeed')
		//but its non issue its not saved
	    String logged_text = get_text_filed(AccountPage.passwords_notsaved);
	    String expected_text = "An error has occurred!";
	    assertEquals(logged_text, expected_text);		
		
	}			
	
	@Test
	public void Account_8() throws Exception {
		//('fill password filed with invalid/long value, should succeed')
		click_account_passwords();
		String password = generate_string(51);
		fill_passwords(password, password);
		//('proper error message, should succeed')
		String logged_text = get_text_filed(AccountPage.passwords_maxpasswdlenght);
		String expected_text = "Your password cannot be longer than 50 characters.";
		assertEquals(logged_text, expected_text);		
		boolean save_btn = element_is_enabled(AccountPage.passwords_save_button);
		assertFalse(save_btn);
		//('fill input fields with valid parameters, should succeed')
		password = generate_string(50);
		fill_passwords(password, password);
		boolean invalid_txt = element_is_displayed(AccountPage.passwords_maxpasswdlenght);
		assertFalse(invalid_txt);
	    save_btn = element_is_enabled(AccountPage.passwords_save_button);
	    assertTrue(save_btn);	
	    click_btn(AccountPage.passwords_save_button);
		//('check save passwords successfully, should succeed')
		//but its non issue its not saved
	    logged_text = get_text_filed(AccountPage.passwords_notsaved);
	    expected_text = "An error has occurred!";
	    assertEquals(logged_text, expected_text);	
	}	
	
	@Test
	public void Account_9() throws Exception {
		//('fill password/confirmed filed with different value, should succeed')
		click_account_passwords();
		String password = generate_string(10);
		String cnf_password = generate_string(5);
		fill_passwords(password, cnf_password);
		//('proper error message, should succeed')
		click_btn(AccountPage.passwords_save_button);
		String logged_text = get_text_filed(AccountPage.passwords_passmissmatch);
		String expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);
		//('fill password/confirmed filed with different value, should succeed')
		password = generate_string(10);
		cnf_password = generate_int(10);
		fill_passwords(password, cnf_password);
		click_btn(AccountPage.passwords_save_button);
		//('proper error message, should succeed')
		logged_text = get_text_filed(AccountPage.passwords_passmissmatch);
		expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);		
		//('fill password/confirmed filed with different value, should succeed')
		password = generate_string(10);
		cnf_password = generate_string(10);
		fill_passwords(password, cnf_password);
		click_btn(AccountPage.passwords_save_button);
		//('proper error message, should succeed')
		logged_text = get_text_filed(AccountPage.passwords_passmissmatch);
		expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);			
		//('fill input fields with valid parameters, should succeed')
		fill_passwords(password, password);	
	    click_btn(AccountPage.passwords_save_button);
		//('check save passwords successfully, should succeed')
		//but its non issue its not saved
	    logged_text = get_text_filed(AccountPage.passwords_notsaved);
	    expected_text = "An error has occurred!";
	    assertEquals(logged_text, expected_text);		
		
	}	
	
	@Test
	public void Account_10() throws Exception {
		//('click invalidate session, should succeed')
		click_btn(AccountPage.account_session);
		int first_count = get_table_count(AccountPage.account_session_table);
		//('sessions table should be reduced by one, should succeed')
		if(first_count != 0){
			invalidate_session();
			String logged_text = get_text_filed(AccountPage.account_session_invalidate);
			String expected_text = "Session invalidated!";
			assertEquals(logged_text, expected_text);
			int last_count = get_table_count(AccountPage.account_session_table);
			assertEquals(first_count, last_count + 1);
			}	
	}
	
	
}