from playwright.sync_api import sync_playwright


# اجرای Chrome با Remote Debugging:
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"


with sync_playwright() as p:

    # اتصال Playwright به Chrome بازشده
    browser = p.chromium.connect_over_cdp(
        "http://localhost:9222"
    )

    # گرفتن context موجود
    context = browser.contexts[0]

    # ساخت یک صفحه جدید
    page = context.new_page()

    # ورود به سایت TSETMC
    page.goto("https://www.tsetmc.com/")

    # کلیک روی نماد فولاد و انتظار برای باز شدن صفحه جدید
    with page.expect_popup() as page1_info:
        page.get_by_role(
            "link",
            name="فولاد",
            exact=True
        ).click()

    # صفحه جدید
    page1 = page1_info.value

    # کمی صبر برای بارگذاری اطلاعات نماد
    page1.wait_for_timeout(3000)

    # -----------------------------
    # قیمت آخرین معامله
    # -----------------------------

    last_price = (
        page1.locator("#d02")
        .inner_text()
        .strip()
    )

    # -----------------------------
    # قیمت پایانی
    # -----------------------------

    closing_price = (
        page1.locator("#d03")
        .inner_text()
        .strip()
    )

    # -----------------------------
    # بیشترین و کمترین قیمت روز
    # -----------------------------

    # پیدا کردن ردیفی که عبارت «بازه روز» دارد
    day_range = page1.locator("tr").filter(
        has_text="بازه روز"
    )

    # گرفتن دو مقدار داخل این ردیف
    values = day_range.locator("[rc-highlight-id]")

    # مقدار اول = بیشترین قیمت
    max_price = (
        values.nth(0)
        .inner_text()
        .strip()
    )

    # مقدار دوم = کمترین قیمت
    min_price = (
        values.nth(1)
        .inner_text()
        .strip()
    )

    # -----------------------------
    # نمایش نتایج
    # -----------------------------

    print("قیمت آخرین معامله:", last_price)
    print("قیمت پایانی:", closing_price)
    print("بیشترین قیمت:", max_price)
    print("کمترین قیمت:", min_price)

    # بستن مرورگر
    browser.close()