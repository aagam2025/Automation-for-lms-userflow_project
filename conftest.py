import pytest
from playwright.sync_api import sync_playwright
from config.config import BASE_URL, HEADLESS, DEVICES, DEFAULT_TIMEOUT_MS

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            slow_mo=50,
        )
        yield browser
        browser.close()

@pytest.fixture(params=[DEVICES["Desktop_1366x768"]], ids=["Desktop_1366x768"])
def device(request):
    return request.param

@pytest.fixture
def page(browser, device):
    context = browser.new_context(
        viewport=device.viewport,
        user_agent=device.user_agent,
        device_scale_factor=device.device_scale_factor,
        # No mobile emulation for desktop
    )
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
    try:
        yield page
    finally:
        page.close()
        context.close()
