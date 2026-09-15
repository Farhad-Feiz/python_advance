from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp(
        "http://localhost:9222"
    )

    context = browser.contexts[0]

    page = context.new_page()

    page.goto(
        "https://www.digikala.com/incredible-offers/"
    )

    page.wait_for_timeout(5000)

    for i in range(3):

        page.mouse.wheel(0, 3000)

        page.wait_for_timeout(3000)

    products = page.locator("h3")

    print("تعداد محصولات پیدا شده:", products.count())

    products_data = []

    count = min(30, products.count())

    for i in range(count):

        name = products.nth(i).inner_text().strip()

        discount = products.nth(i).locator(
            "xpath=ancestor::*[.//span[@data-testid='price-discount-percent']][1]"
        ).locator(
            "span[data-testid='price-discount-percent']"
        ).inner_text().strip()

        products_data.append({
            "name": name,
            "discount": discount
        })

    print("\nنتیجه نهایی:")

    for product in products_data:
        print(product)

    browser.close()