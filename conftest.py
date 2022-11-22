import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_set():
    browser.config.window_height = 800
    browser.config.window_width = 1000
    browser.open('https://google.com')

    yield
    browser.element('[name="q"]').clear()
