package framework;

public class model {

	/**
	 * @param args
	 */
	public interface LoginPage {
		public static final String login = "//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/a";
		public static final String login_text = "//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]";
		public static final String account_menu = ".//*[@id='navbar-collapse']/ul/li[3]/a/span";
		public static final String logout = ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[4]/a/span[2]";
		public static final String rememberme = ".//*[@id='rememberMe']";
		public static final String username = ".//*[@id='username']";
		public static final String password = ".//*[@id='password']";
		public static final String login_button = "//html/body/div[3]/div[1]/div/div/div/form/button";
		public static final String logged = "//html/body/div[3]/div[1]/div/div/div[2]/div/div";                    
		public static final String authentication_error = "//html/body/div[3]/div[1]/div/div/div/div[1]";

	}

	public interface RegistrationPage {
		public static final String register_new_user = "//html/body/div[3]/div[1]/div/div/div[2]/div/div[2]/a";
        public static final String register_login = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input";
        public static final String register_email = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input";
        public static final String register_newpasswd = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/input";
        public static final String register_passwdcfm = "//html/body/div[3]/div[1]/div/div/div/form/div[4]/input";
        public static final String register_button = "// html/body/div[3]/div[1]/div/div/div/form/button";
        public static final String registration_error = "//html/body/div[3]/div[1]/div/div/div/div[2]";
        public static final String registration_loginreq = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[1]";
        public static final String registration_invalidlogin = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[4]";
        public static final String registration_mailreq = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]";
        public static final String registration_invalidmail = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[2]";
        public static final String registration_invalidmaillenght = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[3]";
        public static final String registration_invalidpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[2]";
        public static final String registration_maxpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[3]";
        public static final String registration_passwdreq = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div[1]/p[1]";
        public static final String registration_invalidcnfpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[4]/div/p[2]";
        public static final String registration_cnfpasswdreq = "//html/body/div[3]/div[1]/div/div/div/form/div[4]/div/p[1]";
        public static final String registration_passmissmatch = "//html/body/div[3]/div[1]/div/div/div/div[5]";
        public static final String registration_passbar1 = ".//*[@id='strengthBar']/li[1]";
        public static final String registration_passbar2 = ".//*[@id='strengthBar']/li[2]";
        public static final String registration_passbar3 = ".//*[@id='strengthBar']/li[3]";
        public static final String registration_passbar4 = ".//*[@id='strengthBar']/li[4]";
        public static final String registration_passbar5 = ".//*[@id='strengthBar']/li[5]";

	}	
	
}
