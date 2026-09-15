from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    # اتصال به Chrome
    browser = p.chromium.connect_over_cdp(
        "http://localhost:9222"
    )

    # گرفتن context
    context = browser.contexts[0]

    # ساخت صفحه
    page = context.new_page()

    # باز کردن دیده‌بان بازار
    page.goto(
        "https://old.tsetmc.com/Loader.aspx?ParTree=15131F"
    )

    # صبر برای لود اطلاعات
    page.wait_for_timeout(5000)

    # پیدا کردن نمادها
    symbols = page.locator("a.inst")

    print("تعداد عناصر پیدا شده:", symbols.count())

    stocks = []

    # چون هر نماد دو بار تکرار می‌شود،
    # هر دو عنصر را یک ردیف در نظر نمی‌گیریم.
    count = symbols.count() // 2

    # فقط 10 نماد اول
    count = min(10, count)

    for i in range(count):

        # عنصر مربوط به نماد
        symbol_element = symbols.nth(i * 2)

        # نام نماد
        symbol = symbol_element.inner_text().strip()

        # پیدا کردن div اصلی ردیف
        row = symbol_element.locator("xpath=../..")

        # اطلاعات داخل ردیف
        cells = row.locator("div")

        # حجم
        volume = cells.nth(3).inner_text().strip()

        # آخرین معامله
        last_price = cells.nth(8).inner_text().strip()

        stocks.append({
            "symbol": symbol,
            "last_price": last_price,
            "volume": volume
        })

    # چاپ نتیجه
    print("\nنتیجه نهایی:")

    for stock in stocks:
        print(stock)

    import json

with open("stocks.json", "w", encoding="utf-8") as file:
    json.dump(stocks, file, ensure_ascii=False, indent=4)

print("اطلاعات در فایل stocks.json ذخیره شد.")

browser.close()