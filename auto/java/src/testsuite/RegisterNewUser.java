package testsuite;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import framework.factory;
import framework.model.RegistrationPage;

public class RegisterNewUser extends factory{

	@Before
	public void test_setup() throws Exception {
		click_btn(RegistrationPage.register_new_user);
		Thread.sleep(500);
	}
	
	@Test
	public void Register_New_User_1() throws InterruptedException {
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(RegistrationPage.registration_error);
		String expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}

	@Test
	public void Register_New_User_2() throws InterruptedException {
		String email = generate_string(2);
		fill_register_new_user("login", email, "12345", "12345");
		String logged_text = get_text_filed(RegistrationPage.registration_invalidmail);
		String expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(RegistrationPage.registration_invalidmaillenght);
		expected_text = "Your e-mail is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		email = generate_string(5);
		fill_register_new_user("login", email, "12345", "12345");
		logged_text = get_text_filed(RegistrationPage.registration_invalidmail);
		expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_invalidmaillenght);
		assertFalse(invalid_txt);
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		invalid_txt = element_is_displayed(RegistrationPage.registration_invalidmail);
		assertFalse(invalid_txt);
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}	
	
	@Test
	public void Register_New_User_3() throws InterruptedException {
		fill_register_new_user("login", "+_=-)(*&^#!~`{}[];',.<>/", "12345", "12345");
		String logged_text = get_text_filed(RegistrationPage.registration_invalidmail);
		String expected_text = "Your e-mail is invalid.";
		assertEquals(logged_text, expected_text);
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_invalidmaillenght);
		assertFalse(invalid_txt);	
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		invalid_txt = element_is_displayed(RegistrationPage.registration_invalidmail);
		assertFalse(invalid_txt);		
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}	
	

	@Test
	public void Register_New_User_4() throws InterruptedException {
		String password = generate_string(2);
		fill_register_new_user("login", "email@mail.com", password, password);
		String logged_text = get_text_filed(RegistrationPage.registration_invalidpasswdlenght);
		String expected_text = "Your password is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(RegistrationPage.registration_invalidcnfpasswdlenght);
		expected_text = "Your confirmation password is required to be at least 5 characters.";
		assertEquals(logged_text, expected_text);
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		password = generate_string(5);
		fill_register_new_user("login", "email@mail.com", password, password);
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_invalidpasswdlenght);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(RegistrationPage.registration_invalidcnfpasswdlenght);
		assertFalse(invalid_txt);
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}			
	
  @Test
	public void Register_New_User_5() throws InterruptedException {
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		fill_register_new_user("", "", "", "");
		String logged_text = get_text_filed(RegistrationPage.registration_loginreq);
		String expected_text = "Your login is required.";
		assertEquals(logged_text, expected_text);		
		logged_text = get_text_filed(RegistrationPage.registration_mailreq);
		expected_text = "Your e-mail is required.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(RegistrationPage.registration_passwdreq);
		expected_text = "Your password is required.";
		assertEquals(logged_text, expected_text);
		logged_text = get_text_filed(RegistrationPage.registration_cnfpasswdreq);
		expected_text = "Your confirmation password is required.";		
		assertEquals(logged_text, expected_text);
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_loginreq);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(RegistrationPage.registration_mailreq);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(RegistrationPage.registration_passwdreq);
		assertFalse(invalid_txt);
		invalid_txt = element_is_displayed(RegistrationPage.registration_cnfpasswdreq);
		assertFalse(invalid_txt);		
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}		
	
	@Test
	public void Register_New_User_6() throws InterruptedException {
		fill_register_new_user("login", "email@mail.com", "12345", "12345");
		String bar_color = element_background_color(RegistrationPage.registration_passbar1);
		String expected_color = "rgba(255, 0, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(RegistrationPage.registration_passbar2);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar3);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar4);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		
		fill_register_new_user("login", "email@mail.com", "12345abcde", "12345abcde");
		bar_color = element_background_color(RegistrationPage.registration_passbar1);
		expected_color = "rgba(255, 153, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(RegistrationPage.registration_passbar2);
		expected_color = "rgba(255, 153, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar3);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar4);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		
		fill_register_new_user("login", "email@mail.com", "12345abcdeABC", "12345abcdeABC");
		bar_color = element_background_color(RegistrationPage.registration_passbar1);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(RegistrationPage.registration_passbar2);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar3);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar4);
		expected_color = "rgba(153, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar5);
		expected_color = "rgba(221, 221, 221, 1)";
		assertEquals(bar_color, expected_color);		
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);		

		fill_register_new_user("login", "email@mail.com", "12345abcdeABC!", "12345abcdeABC!");
		bar_color = element_background_color(RegistrationPage.registration_passbar1);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
		bar_color = element_background_color(RegistrationPage.registration_passbar2);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar3);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar4);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);
		bar_color = element_background_color(RegistrationPage.registration_passbar5);
		expected_color = "rgba(0, 255, 0, 1)";
		assertEquals(bar_color, expected_color);		
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);		
		
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(RegistrationPage.registration_error);
		String expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);		
		
	}			
	
	@Test
	public void Register_New_User_7() throws InterruptedException {
		String password = generate_string(51);
		fill_register_new_user("login", "email@mail.com", password, password);
		String logged_text = get_text_filed(RegistrationPage.registration_maxpasswdlenght);
		String expected_text = "Your password cannot be longer than 50 characters.";
		assertEquals(logged_text, expected_text);		
		boolean register_btn = element_is_enabled(RegistrationPage.register_button);
		assertFalse(register_btn);
		
		password = generate_string(50);
		fill_register_new_user("login", "email@mail.com", password, password);
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_maxpasswdlenght);
		assertFalse(invalid_txt);
		register_btn = element_is_enabled(RegistrationPage.register_button);
		assertTrue(register_btn);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);
	}	
	
	@Test
	public void Register_New_User_8() throws InterruptedException {
		String password = generate_string(10);
		String cnf_password = generate_string(5);
		fill_register_new_user("login", "email@mail.com", password, cnf_password);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(RegistrationPage.registration_passmissmatch);
		String expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);
		
		password = generate_string(10);
		cnf_password = generate_int(10);
		fill_register_new_user("login", "email@mail.com", password, cnf_password);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_passmissmatch);
		expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);		
		
		password = generate_string(10);
		cnf_password = generate_string(10);
		fill_register_new_user("login", "email@mail.com", password, cnf_password);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		logged_text = get_text_filed(RegistrationPage.registration_passmissmatch);
		expected_text = "The password and its confirmation do not match!";
		assertEquals(logged_text, expected_text);			
		
		fill_register_new_user("login", "email@mail.com", password, password);
		click_btn(RegistrationPage.register_button);
		Thread.sleep(500);
		boolean invalid_txt = element_is_displayed(RegistrationPage.registration_passmissmatch);
		assertFalse(invalid_txt);		
		logged_text = get_text_filed(RegistrationPage.registration_error);
		expected_text = "Registration failed! Please try again later.";
		assertEquals(logged_text, expected_text);		
		
	}
	
}
