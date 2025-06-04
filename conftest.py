import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Открывает браузер с интерфейсом для отладки
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()

