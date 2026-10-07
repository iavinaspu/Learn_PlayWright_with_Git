import re

from playwright.sync_api import Page, expect


def test_verifyurl(page:Page):
    page.goto("https://in.bookmyshow.com/")
    expect(page).to_have_url("https://in.bookmyshow.com/")

def test_Title(page:Page):
    page.goto("https://in.bookmyshow.com/")
    expect(page).to_have_title("Movie Tickets, Plays, Sports, Events & Cinemas nearby - BookMyShow")

def test_SelectPune(page:Page):
    page.goto("https://in.bookmyshow.com/")
    logo=page.get_by_alt_text("Pune")
    logo.click()
    expect(logo).to_be_visible()

def test_clickbutton(page:Page):
    page.goto("https://in.bookmyshow.com/")
    logo=page.get_by_alt_text("Pune")
    logo.click()
    expect(logo).to_be_visible()
    lg=page.get_by_alt_text("Drishyam The Conclusion")
    lg.click()
    page.get_by_role("button", name=re.compile("Book tickets",re.IGNORECASE)).click()



