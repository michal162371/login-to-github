from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utilities.config import EMAIL , PASSWORD


def test_sign_in_to_git(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    signInPage.sign_in_button()
    signInPage.wait_for_sign_in_button()
    assert EMAIL is not None, "TEST_EMAIL environment variable is not set"
    signInPage.email_input.fill(EMAIL)
    assert PASSWORD is not None, "TEST_PASSWORD environment variable is not set"
    signInPage.password_input.fill(PASSWORD)
    expect (signInPage.signWithCredentialsButton).to_be_visible()
    pass 