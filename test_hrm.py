from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    login_button = page.get_by_role("button", name="Login")

    username.fill("Admin")
    password.fill("admin123")
    login_button.click()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.get_by_role("link", name="Buzz").click()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")

