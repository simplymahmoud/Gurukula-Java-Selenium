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
	
	public interface AccountPage {
		public static final String account_settings = ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[1]/a/span[2]";
		public static final String settings_title = "//html/body/div[3]/div[1]/div/div/div/h2";
		public static final String settings_firstname = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input";
		public static final String settings_firstnamereq = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div/p[1]";
		public static final String settings_lastname = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input";
		public static final String settings_lastnamereq = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]";
		public static final String settings_email = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/input";
		public static final String settings_invalidmail = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[2]";
		public static final String settings_invalidmaillenght = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[3]";
		public static final String settings_mailreq = "//html/body/div[3]/div[1]/div/div/div/form/div[3]/div/p[1]";
		public static final String settings_language = "//html/body/div[3]/div[1]/div/div/div/form/div[4]/select";
		public static final String settings_save_button = "//html/body/div[3]/div[1]/div/div/div/form/button";
		public static final String settings_saved = "//html/body/div[3]/div[1]/div/div/div/div[1]";
		public static final String settings_notsaved = "//html/body/div[3]/div[1]/div/div/div/div[3]/strong";
		public static final String account_passwords = ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[2]/a/span[2]";
		public static final String passwords_title = "//html/body/div[3]/div[1]/div/div/div/h2";
		public static final String passwords_newpasswd = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/input";
		public static final String passwords_invalidpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[2]";
		public static final String passwords_passwdreq = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[1]";
		public static final String passwords_maxpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[1]/div[1]/p[3]";
		public static final String passwords_passwdcnf = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/input";
		public static final String passwords_invalidpasswdcnflenght = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[2]";
		public static final String passwords_passwdcnfreq = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[1]";
		public static final String passwords_maxcnfpasswdlenght = "//html/body/div[3]/div[1]/div/div/div/form/div[2]/div/p[3]";
		public static final String passwords_save_button = "//html/body/div[3]/div[1]/div/div/div/form/button";
		public static final String passwords_notsaved = "//html/body/div[3]/div[1]/div/div/div/div[2]/strong";
		public static final String passwords_passmissmatch = "//html/body/div[3]/div[1]/div/div/div/div[3]";
		public static final String account_session = ".//*[@id='navbar-collapse']/ul/li[3]/ul/li[3]/a/span[2]";
		public static final String account_session_table = "//html/body/div[3]/div[1]/div/div[3]/table";
		public static final String account_session_invalidate = "//html/body/div[3]/div[1]/div/div[1]";		
        public static final String passwords_passbar1 = ".//*[@id='strengthBar']/li[1]";
        public static final String passwords_passbar2 = ".//*[@id='strengthBar']/li[2]";
        public static final String passwords_passbar3 = ".//*[@id='strengthBar']/li[3]";
        public static final String passwords_passbar4 = ".//*[@id='strengthBar']/li[4]";
        public static final String passwords_passbar5 = ".//*[@id='strengthBar']/li[5]";
	}		
	
	public interface BranchPage {
		public static final String entities_menu = ".//*[@id='navbar-collapse']/ul/li[2]/a/span/span[2]";
		public static final String entities_branch = ".//*[@id='navbar-collapse']/ul/li[2]/ul/li[1]/a/span[2]";
		public static final String create_new_branch_button = "//html/body/div[3]/div[1]/div/div[1]/div/div[1]/button";
		public static final String search_branch_button = "//html/body/div[3]/div[1]/div/div[1]/div/div[2]/form/button";
		public static final String new_branch_id = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[1]/input";
		public static final String new_branch_name = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/input";
		public static final String new_branch_name_req = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[1]";
		public static final String new_branch_name_invalid_length = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[2]";
		public static final String new_branch_name_invalid = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[4]";
		public static final String new_branch_name_invalid_maxlength = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/div/p[3]";
		public static final String new_branch_code = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/input";
		public static final String new_branch_code_req = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[1]";
		public static final String new_branch_code_invalid_length = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[2]";
		public static final String new_branch_code_invalid = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[4]";
		public static final String new_branch_code_invalid_maxlength = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[3]/div/p[3]";
		public static final String cancel_branch_button = ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[1]";
		public static final String save_branch_button = ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[2]";
		public static final String search_branch_text = ".//*[@id='searchQuery']";
		public static final String search_branch_cancel_delete = ".//*[@id='deleteBranchConfirmation']/div/div/form/div[3]/button[1]";
		public static final String search_branch_confirm_delete = ".//*[@id='deleteBranchConfirmation']/div/div/form/div[3]/button[2]";
		public static final String search_branch_table = "//html/body/div[3]/div[1]/div/div[4]/table";
		public static final String search_branch_view_name = "//html/body/div[3]/div[1]/div/div/table/tbody/tr[1]/td[2]/input";
		public static final String search_branch_view_code = "//html/body/div[3]/div[1]/div/div/table/tbody/tr[2]/td[2]/input";
		public static final String view_back_button = "//html/body/div[3]/div[1]/div/button";
		public static final String edit_branch_name = ".//*[@id='saveBranchModal']/div/div/form/div[2]/div[2]/input";
		public static final String save_edit_branch_button = ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[2]";
		public static final String cancel_edit_branch_button = ".//*[@id='saveBranchModal']/div/div/form/div[3]/button[1]";

	}	
	
	public interface StaffPage {
		public static final String entities_menu = ".//*[@id='navbar-collapse']/ul/li[2]/a/span/span[2]";
		public static final String entities_branch = ".//*[@id='navbar-collapse']/ul/li[2]/ul/li[1]/a/span[2]";
		public static final String entities_staff = ".//*[@id='navbar-collapse']/ul/li[2]/ul/li[2]/a/span[2]";		
		public static final String new_staff_id = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[1]/input";
		public static final String new_staff_name = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/input";
		public static final String new_staff_name_req = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[1]";
		public static final String new_staff_name_invalid = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[4]";
		public static final String new_staff_name_invalid_maxlength = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[2]/div/p[3]";
		public static final String staff_dropdown = ".//*[@id='saveStaffModal']/div/div/form/div[2]/div[3]/select";
		public static final String save_staff_button = ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[2]";
		public static final String search_staff_confirm_delete = ".//*[@id='deleteStaffConfirmation']/div/div/form/div[3]/button[2]";
		public static final String cancel_staff_button = ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[1]";
		public static final String search_staff_view_name = "//html/body/div[3]/div[1]/div/div/table/tbody/tr[1]/td[2]/input";
		public static final String search_staff_view_branch = "//html/body/div[3]/div[1]/div/div/table/tbody/tr[2]/td[2]/input";
		public static final String save_edit_staff_button = ".//*[@id='saveStaffModal']/div/div/form/div[3]/button[2]";
		public static final String search_staff_table = "//html/body/div[3]/div[1]/div/div[4]/table";
		public static final String staff_paging_first_page = "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[1]/a";
		public static final String staff_paging_previos_page = "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[2]/a";
		public static final String staff_paging_next_page = "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[3]/a";
		public static final String staff_paging_last_page = "//html/body/div[3]/div[1]/div/div[4]/nav/ul/li[4]/a";

	}	
	
}
