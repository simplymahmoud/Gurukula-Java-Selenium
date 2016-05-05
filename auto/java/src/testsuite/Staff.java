package testsuite;

import org.junit.Before;

import framework.factory;

public class Staff extends factory{

	@Before
	public void test_setup() throws Exception {
		click_login();
		fill_login("admin", "admin");
		click_authenticat();
		click_account_menu();
	}

}
