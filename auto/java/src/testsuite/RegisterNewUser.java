package testsuite;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import framework.factory;
import framework.model.RegistrationPage;

public class RegisterNewUser  extends factory{

	@Before
	public void go_home() throws Exception {
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

}
