import os
from SbisSite import SearchHelper
from selenium.webdriver.common.by import By
import time
import math


def test_sbis(browser):
    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    sbis_main_page = SearchHelper(browser)
# Открываем сайт
    sbis_main_page.go_to_site()
# В Footer находим опцию "Скачать СБИС" и нажимаем на неё
    download_button_reference = 'Скачать СБИС'
    download_button = (sbis_main_page.get_footer()
                       .find_element(By.XPATH, "//a[contains(text(),'{}')]".format(download_button_reference)))
    sbis_main_page.scroll_to_the_element(download_button)
    time.sleep(1)
    download_button.click()
    time.sleep(2)
    assert 'download' in sbis_main_page.get_current_url()
# На вкладке Downloads в левом столбце находим опцию "СБИС Плагин", выбираем её
    tab_button_name = 'СБИС Плагин'
    tab_button = (sbis_main_page.tab_buttons()
                  .find_element(By.XPATH, "//div/div/div/div[contains(text(),'{}')]".format(tab_button_name)))
    sbis_main_page.hover_over(tab_button)
    sbis_main_page.click_elusive_element(tab_button)
    time.sleep(2)
# Находим и скачиваем Веб-установщик
    option_name = 'Веб-установщик'
    sbis_main_page.list_of_downloads().find_element(By.XPATH, "//div[descendant::h3[contains(text(), '{}')] "
                                                              "and contains(@class, 'sbis_ru-DownloadNew-block')]//a".format(option_name)).click()
    time.sleep(5)
# Проверяем размер скаченного файла
    expected_size = ['3.65 MB', '3.64 MB', '3.66 MB', '3.67 MB', '3.68 MB']
    downloaded_file = f'data/{os.listdir("data/")[0]}'
    assert convert_size(os.path.getsize(downloaded_file)) in expected_size
