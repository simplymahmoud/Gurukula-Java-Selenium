package framework;


import org.junit.After;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import framework.model.RegistrationPage;


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
	
	public String get_text_filed (String field) {
		String content="";
		try {
			content = (String) driver.findElement(By.xpath(field)).getText();
		} catch (org.openqa.selenium.ElementNotVisibleException e) {
			System.out.println(e);
		}
		return content;
	}
	
	public void click_btn(String selector) {
		WebElement webElement = driver.findElement(By.xpath(selector));
		webElement.click();
	}	
	
	public void fill_register_new_user (String login, String email, String newpasswd, String passwdcfm) {
		set_text_field(RegistrationPage.register_login, login);
		set_text_field(RegistrationPage.register_email, email);
		set_text_field(RegistrationPage.register_newpasswd, newpasswd);
		set_text_field(RegistrationPage.register_passwdcfm, passwdcfm);	
	}
	
	public void clean_driver() {
		this.driver.quit();
	}

	@After
	public void tearDown() throws Exception {
		clean_driver();
	}	
	
}