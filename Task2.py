from SbisSite import SearchHelper
from selenium.webdriver.common.by import By
import time


def test_sbis(browser):
    sbis_main_page = SearchHelper(browser)
# Открываем сайт
    sbis_main_page.go_to_site()
# Проверяем наличие городом из моего региона в списке контактов
    cities_kostroma = ['Кострома', 'Нея']
    for c in cities_kostroma:
        assert c in [x.text for x in sbis_main_page.get_city_names()]
# Открываем список всех регионов, выбираем нужный
    new_region = 'Камчатский край'
    cities_kamchatka = ['Петропавловск-Камчатский']
    sbis_main_page.open_region_chooser()
    region_panel = sbis_main_page.get_region_chooser_panel()
    region_panel.find_element(By.XPATH, "//li/span[contains(@title,'{}')]".format(new_region)).click()
    time.sleep(2)
# Проверяем что url, title и список городов показывают корректную информацию
    assert '41-kamchatskij-kraj' in sbis_main_page.get_current_url()
    for c in cities_kamchatka:
        assert c in [x.text for x in sbis_main_page.get_city_names()]
    assert new_region in sbis_main_page.get_page_title()
