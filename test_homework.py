from selene.support.shared import browser
from selene import be, have

def test_search_positive(browser_set):

    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))

def test_search_negative(browser_set):

    browser.element('[name="q"]').should(be.blank).type('hgjdjfhgjgjhfdj').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))