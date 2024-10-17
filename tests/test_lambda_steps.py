import allure
from selene.support.shared import browser
from selene.support.conditions.have import exact_text
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_github():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Таб issue')
    allure.dynamic.story('Наименование issue')
    allure.dynamic.link('https://github.com', name='testing')

    with allure.step('Открываем странице с репозиторием'):
        browser.open("https://github.com/Nastya-Leto/HW_allure_10")

    with allure.step('Открываем таб issues'):
        s("#issues-tab").click()

    with allure.step('Проверяем названия issue'):
        s('#issue_1_link').should(exact_text('Enjoy autumn'))
