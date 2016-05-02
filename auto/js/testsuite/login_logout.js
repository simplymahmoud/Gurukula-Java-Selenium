describe('Test using Protractor(jasmine)', function() {
    var login_page = element(by.xpath("//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/a"));
    var login_username = element(by.xpath(".//*[@id='username']"));
    var login_password = element(by.xpath(".//*[@id='password']"));
    var login_button = element(by.xpath("//html/body/div[3]/div[1]/div/div/div/form/button"));
    var logged_msg = element(by.xpath("//html/body/div[3]/div[1]/div/div/div[2]/div/div"));
    var account_menu = element(by.xpath(".//*[@id='navbar-collapse']/ul/li[3]/a/span"));
    var logout = element(by.xpath(".//*[@id='navbar-collapse']/ul/li[3]/ul/li[4]/a/span[2]"));
    var login_txt = element(by.xpath("//html/body/div[3]/div[1]/div/div/div[2]/div/div[1]"));
    
  function do_login(username, password) {
    login_username.sendKeys(username);
    login_password.sendKeys(password);
    login_button.click();
  }    
    
  function sleep(milliseconds) {
    var start = new Date().getTime();
    var timer = true;
    while (timer) {
        if ((new Date().getTime() - start)> milliseconds) {
            timer = false;
        }
      }
    }    
    
  beforeEach(function() {
    browser.get('http://127.0.0.1:8080/gurukula');
  });    

  it('should login/logout', function() {
    expect(login_txt.getText()).toEqual('Click here to login');
    login_page.click();
    do_login('admin', 'admin');
    expect(logged_msg.getText()).toEqual('You are logged in as user "admin".');
    account_menu.click();
    logout.click();
    expect(login_txt.getText()).toEqual('Click here to login');
  });        

});
