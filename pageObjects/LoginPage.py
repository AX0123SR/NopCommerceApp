'''
Under pageObjects, we have to create a class where we have to store all Locators.
Then create a constructor __init__ which automatically call when the object has created.
Finally we have to create Action methods for each Locators.
'''


class LoginPage:
    textbox_username_xpath = "//input[@class = 'email']"
    textbox_password_xpath = "//input[@class = 'password']"
    button_Login_xpath = "//button[contains(text(), 'Log in')]"
    link_Logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys("admin@yourstore.com")

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys("admin")

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_Logout_linktext).click()
