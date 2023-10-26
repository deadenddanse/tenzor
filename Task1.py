from SbisSite import SearchHelper
from selenium.webdriver.common.by import By


def test_sbis(browser):
    sbis_main_page = SearchHelper(browser)
# Открываем сайт
    sbis_main_page.go_to_site()
# Находим и кликаем на баннер "Тензор"
    sbis_main_page.click_on_the_banner()
# Открывается новая таба, переходим на неё и проверяем что новая таба та что мы хотели увидеть
    sbis_main_page.switch_tab()
    assert sbis_main_page.get_current_url() == 'https://tensor.ru/'
# Находим все блоки с информацией и проверяем что есть блок с текстом "Сила в людях"
    blocks = sbis_main_page.get_all_info_blocks()
    block_found = -1
    for block in [x.text for x in blocks]:
        if 'Сила в людях' in block.splitlines():
            block_found = [x.text for x in blocks].index(block)
    assert block_found != -1
# В найденом выше блоке находим кнопку "подробнее", нажимаем на неё, проверяем что перешли на ожидаемую страницу
    blocks[block_found].find_element(By.XPATH, "//a[@href='/about']").click()
    assert sbis_main_page.get_current_url() == 'https://tensor.ru/about'
# Находим блок фотографий, проверяем на однородность
    photos = sbis_main_page.get_photos()
    for single_photo in photos:
        assert list(single_photo.size.values()) == list(photos[0].size.values())




