package testsuite;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import framework.factory;
import framework.model.LoginPage;


public class LoginLogout extends factory{

	@Before
	public void test_setup() throws Exception {
		click_login();
	}		
	
	@Test
	public void Login_Logout_1() throws Exception {
		fill_login("admin", "admin");
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.logged);
		String expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
	}

	@Test
	public void Login_Logout_2() throws Exception {
		fill_login("admin", "admin");
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.logged);
		String expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
	}	
	
	@Test
	public void Login_Logout_3() throws Exception {
		String username = generate_string(5);
		fill_login(username, "admin");
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		
		fill_login("admin", "admin");
		click_authenticat();
		logged_text = get_text_filed(LoginPage.logged);
		expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
	}	

	@Test
	public void Login_Logout_4() throws Exception {
		String password = generate_string(5);
		fill_login("admin", password);
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		
		fill_login("admin", "admin");
		click_authenticat();
		logged_text = get_text_filed(LoginPage.logged);
		expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
	}		
	
	@Test
	public void Login_Logout_5() throws Exception {
		String username = generate_string(5);
		String password = generate_string(5);
		fill_login(username, password);
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		
		fill_login("admin", "admin");
		click_authenticat();
		logged_text = get_text_filed(LoginPage.logged);
		expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
	}	
	
	@Test
	public void Login_Logout_6() throws Exception {
		click_btn(LoginPage.rememberme);
		fill_login("admin", "admin");
		click_authenticat();
		String logged_text = get_text_filed(LoginPage.logged);
		String expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
		click_btn(LoginPage.login);
		
		fill_login("admin", "");
		click_authenticat();
		logged_text = get_text_filed(LoginPage.authentication_error);
		expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);				
	}		
	
}
