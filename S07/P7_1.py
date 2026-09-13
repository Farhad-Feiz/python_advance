import json
from playwright.sync_api import sync_playwright

# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    context = browser.contexts[0]
    page = context.new_page()
    # ورود به ترب

    page.goto('https://torob.com/')


    page.get_by_test_id("search-query").click()
    page.get_by_test_id("search-query").fill("لپتاپ ایسوس")
    page.get_by_test_id("search-query").press("Enter")


    # صبر برای لود نتایج

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(5000)
    products = []


    # پیدا کردن لینک‌های محصولات

    cards = page.locator('[class*="ProductCard_desktop_card"]')


    print("Product cards:", cards.count())


    for i in range(min(10, cards.count())):
        card = cards.nth(i)


        href = card.locator("a").first.get_attribute("href")
        if not href:
            continue
        title = card.inner_text().strip()
        image = card.locator("picture img").first
        src = image.get_attribute("src") if image.count() else None
        print(src)
        products.append({"title": title, "href": href, "src": src})
    # ذخیره در JSON
    with open("torob_products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
    print("Data are saved")
    browser.close()