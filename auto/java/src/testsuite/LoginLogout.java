package testsuite;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import framework.factory;
import framework.model.LoginPage;


public class LoginLogout extends factory{

	@Before
	public void go_home() throws Exception {
		click_btn(LoginPage.login);
		Thread.sleep(500);
	}		
	
	@Test
	public void Login_Logout_1() throws InterruptedException {
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(LoginPage.logged);
		String expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
	}

	@Test
	public void Login_Logout_2() throws InterruptedException {
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
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
	public void Login_Logout_3() throws InterruptedException {
		set_text_field(LoginPage.username, "wrong");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
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
	public void Login_Logout_4() throws InterruptedException {
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "wrong");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
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
	public void Login_Logout_5() throws InterruptedException {
		set_text_field(LoginPage.username, "wrong");
		set_text_field(LoginPage.password, "wrong");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(LoginPage.authentication_error);
		String expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
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
		set_text_field(LoginPage.username, "admin");
		set_text_field(LoginPage.password, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		String logged_text = get_text_filed(LoginPage.logged);
		String expected_text = "You are logged in as user \"admin\".";
		assertEquals(logged_text, expected_text);
		click_btn(LoginPage.account_menu);
		click_btn(LoginPage.logout);
		Thread.sleep(500);
		String logout_text = get_text_filed(LoginPage.login_text);
		expected_text = "Click here to login";	
		assertEquals(logout_text, expected_text);
		click_btn(LoginPage.login);
		Thread.sleep(500);
		set_text_field(LoginPage.username, "admin");
		click_btn(LoginPage.login_button);
		Thread.sleep(500);
		logged_text = get_text_filed(LoginPage.authentication_error);
		expected_text = "Authentication failed! Please check your credentials and try again.";
		assertEquals(logged_text, expected_text);				
	}		
	
}
