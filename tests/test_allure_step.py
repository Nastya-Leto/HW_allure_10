import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support.conditions.have import exact_text
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", 'zakharovaaa')
@allure.feature('Таб issue')
@allure.story('Наименование issue')
@allure.link('https://github.com', name='testing')
def test_github():
    open_page()
    open_tab()
    should_name_issue()


@allure.step('Открываем странице с репозиторием')
def open_page():
    browser.open("https://github.com/Nastya-Leto/HW_allure_10")


@allure.step('Открываем таб issues')
def open_tab():
    s("#issues-tab").click()


@allure.step('Проверяем названия issue')
def should_name_issue():
    s('#issue_1_link').should(exact_text('Enjoy autumn'))
