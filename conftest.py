import pytest
from playwright.sync_api import sync_playwright
import allure

@pytest.fixture(scope="module")
def page():
    with allure.step("Запуск Playwright и создание страницы"):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            yield page

            with allure.step("Закрытие страницы, контекста и браузера"):
                page.close()
                context.close()
                browser.close()