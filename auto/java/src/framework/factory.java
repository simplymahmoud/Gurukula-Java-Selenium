package framework;


import java.util.List;

import org.apache.commons.lang3.RandomStringUtils;
import org.junit.After;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import framework.model.LoginPage;
import framework.model.RegistrationPage;
import framework.model.AccountPage;
import framework.model.BranchPage;
//import framework.model.StaffPage;


public class factory {
	public WebDriver driver;

	public factory() {
		driver = new FirefoxDriver();
		driver.get("http://127.0.0.1:8080/gurukula");
		driver.manage().window().maximize();
	}


	public void set_text_field(String field, String text) {
		try {
			WebElement textfield = driver.findElement(By.xpath(field));
			textfield.clear();
			textfield.sendKeys(text);
		} catch (org.openqa.selenium.ElementNotVisibleException e) {
			System.out.println(e);
		}
	}	
	
	public String get_text_filed (String selector) {
		String content="";
		try {
			content = (String) driver.findElement(By.xpath(selector)).getText();
		} catch (org.openqa.selenium.ElementNotVisibleException e) {
			System.out.println(e);
		}
		return content;
	}
	
	public void click_btn(String selector) throws Exception {
		WebElement webElement = driver.findElement(By.xpath(selector));
		webElement.click();
		Thread.sleep(500);
	}	
	
	public boolean element_is_enabled(String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
		return webElement.isEnabled();
	}	
	
	public boolean element_is_displayed(String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
		return webElement.isDisplayed();
	}		

	public boolean element_is_readonly(String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
		return webElement.getAttribute("readOnly").equals("true");
	}	
	
	public String element_background_color (String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
	    return webElement.getCssValue("background-color");
	}	
	
	public WebElement get_table (String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
		return webElement;
	}	
	
	public int get_table_count (String selector) {
		WebElement table = get_table(selector);
		List<WebElement> tbody = table.findElements(By.tagName("tbody"));
		List<WebElement> rows = tbody.get(0).findElements(By.tagName("tr"));
		return rows.size();
	}	
	
	public void invalidate_session() throws Exception {
		WebElement table = get_table(AccountPage.account_session_table);
		List<WebElement> tbody = table.findElements(By.tagName("tbody"));
		List<WebElement> rows = tbody.get(0).findElements(By.tagName("tr"));
		
		 if(rows.size() != 0){
			 List<WebElement> cells = rows.get(0).findElements(By.tagName("td"));
			 cells.get(3).findElements(By.tagName("button")).get(0).click();
			 Thread.sleep(500);
		  } 
	}	
	
	public Boolean search_branch (String branch) throws Exception {
		set_text_field(BranchPage.search_branch_text, branch);
		click_search_branch();
		WebElement table = get_table(BranchPage.search_branch_table);
		List<WebElement> tbody = table.findElements(By.tagName("tbody"));
		List<WebElement> rows = tbody.get(0).findElements(By.tagName("tr"));
		
		if(rows.size() != 0){
			 return true;
		} 
		return false;
	}		
	
	public void delete_branch (String branch) throws Exception {
		set_text_field(BranchPage.search_branch_text, branch);
		click_search_branch();
		WebElement table = get_table(BranchPage.search_branch_table);
		List<WebElement> tbody = table.findElements(By.tagName("tbody"));
		List<WebElement> rows = tbody.get(0).findElements(By.tagName("tr"));
		
		 if(rows.size() != 0){
			 List<WebElement> cells = rows.get(0).findElements(By.tagName("td"));
			 cells.get(3).findElements(By.tagName("button")).get(2).click();
			 Thread.sleep(500);
			 click_btn(BranchPage.search_branch_confirm_delete);
		  } 
	}	
	
	public void fill_login (String username, String password) {
		set_text_field(LoginPage.username, username);
		set_text_field(LoginPage.password, password);
	}	
	
	public void fill_register_new_user (String login, String email, String newpasswd, String passwdcfm) {
		set_text_field(RegistrationPage.register_login, login);
		set_text_field(RegistrationPage.register_email, email);
		set_text_field(RegistrationPage.register_newpasswd, newpasswd);
		set_text_field(RegistrationPage.register_passwdcfm, passwdcfm);	
	}	

	public void fill_settings (String firstname, String lastname, String email) {
		set_text_field(AccountPage.settings_firstname, firstname);
		set_text_field(AccountPage.settings_lastname, lastname);
		set_text_field(AccountPage.settings_email, email);
	}	
	
	public void fill_passwords (String newpasswd, String passwdcfm) {
		set_text_field(AccountPage.passwords_newpasswd, newpasswd);
		set_text_field(AccountPage.passwords_passwdcnf, passwdcfm);
	}		
	
	public void fill_new_branch (String branch, String code) throws Exception {
		set_text_field(BranchPage.new_branch_name, branch);
		set_text_field(BranchPage.new_branch_code, code);
		Thread.sleep(500);
	}		
	
	public void clean_driver() {
		this.driver.quit();
	}

	@After
	public void tearDown() throws Exception {
		clean_driver();
	}	
	
	public void click_login() throws Exception {
		click_btn(LoginPage.login);
	}	
	
	public void click_authenticat() throws Exception {
		click_btn(LoginPage.login_button);
	}	
	
	public void click_account_menu() throws Exception {
		click_btn(LoginPage.account_menu);
	}
	
	public void click_account_settings() throws Exception {
		click_btn(AccountPage.account_settings);
	}	
	
	public void click_account_passwords() throws Exception {
		click_btn(AccountPage.account_passwords);
	}		
	
	public void click_entities_branch_menu() throws Exception {
		click_btn(BranchPage.entities_menu);
		click_btn(BranchPage.entities_branch);
	}		
	
	public void click_create_new_branch() throws Exception {
		click_btn(BranchPage.create_new_branch_button);
	}		
	
	public void click_save_branch() throws Exception {
		click_btn(BranchPage.save_branch_button);
	}	
	
	public void click_search_branch() throws Exception {
		click_btn(BranchPage.search_branch_button);
	}	
	
	public String generate_string(int lenght) {
		return RandomStringUtils.randomAlphabetic(lenght);
	}	
	
	public String generate_int(int lenght) {
		return RandomStringUtils.randomNumeric(lenght);
	}	
	
}