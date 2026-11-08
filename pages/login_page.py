from playwright.sync_api import  Locator, Page
from pages.base_page import BasePage
from utilities import config

class LoginPage(BasePage):
    PATH = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def signInButton(self) -> Locator: 
        return self.page.get_by_role("link", name="Sign in")  
    @property
    def email_input(self) -> Locator: 
            return self.page.get_by_role("textbox", name="username or email address")  
    @property
    def password_input(self) -> Locator: 
            return self.page.get_by_role("textbox", name="password")  
    @property
    def signWithCredentialsButton(self) -> Locator: 
            return self.page.get_by_role("button", name="Sign in", exact=True)  

    
    def sign_in_button(self):
        self.signInButton.click()

    def wait_for_sign_in_button(self):
        self.page.wait_for_url("**/login")    


    