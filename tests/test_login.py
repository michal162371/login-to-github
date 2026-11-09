from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utilities.config import TEST_EMAIL, TEST_PASSWORD


def test_sign_in_to_git(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()
    page.pause()
    signInPage.sign_in_button()
    signInPage.wait_for_sign_in_button()
    assert TEST_EMAIL is not None, "TEST_EMAIL environment variable is not set"
    signInPage.email_input.fill(TEST_EMAIL)
    assert TEST_PASSWORD is not None, "TEST_PASSWORD environment variable is not set"
    signInPage.password_input.fill(TEST_PASSWORD)
    expect (signInPage.signWithCredentialsButton).to_be_visible()
    pass 