from selene.support.conditions.have import exact_text
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com/Nastya-Leto/HW_allure_10")

    s("#issues-tab").click()

    s('#issue_1_link').should(exact_text('Enjoy autumn'))
