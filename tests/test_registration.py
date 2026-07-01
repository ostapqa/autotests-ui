from playwright.sync_api import expect, Page


def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    email.fill('user.name@gmail.com')

    username = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    username.fill('username')

    password = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    password.fill('password')

    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    chromium_page.wait_for_timeout(5000)