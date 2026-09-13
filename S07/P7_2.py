import json
from playwright.sync_api import sync_playwright

# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    context = browser.contexts[0]
    page = context.new_page()
    # ورود به سامانه بورس

    page.goto('https://www.tsetmc.com/')

    # page.get_by_role("link", name="فولاد", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="فولاد", exact=True).click()
    page1 = page1_info.value
    print("PAGE 1 URL:", page1.url)

    print("de2:", page1.locator("#d02").count())
    print("de3:", page1.locator("#d03").count())
    page1.wait_for_timeout(300)
    # قیمت آخرین معامله      
    last_price = page1.locator(
        "#d02"
            ).inner_text().strip()
    # قیمت پایانی
    closing_price = page1.locator(
        "#d03"
    ).inner_text().strip()
   # بازه روز
day_range = page1.locator("tr").filter(has_text="بازه روز")
values = day_range.locator("[rc-highlight-id]")

max_price = values.nth(0).inner_text().strip()
min_price = values.nth(1).inner_text().strip()

    print("قیمت پایانی:", closing_price)
    print("بیشترین قیمت:", max_price)
    print("کمترین قیمت:", min_price)
    print("قیمت آخرین معامله:", last_price)

    browser.close()
    page.pause()