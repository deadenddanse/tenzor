from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisSearchLocators:
    LOCATOR_SBIS_NAVIGATION_BAR = (By.CSS_SELECTOR, ".tensor_ru-Header__centered")
    LOCATOR_SBIS_TENSOR_BANNER = (By.XPATH, "//a[@title='tensor.ru']")
    LOCATOR_SBIS_BLOCKS = (By.XPATH,
                           "//div[contains(@class, 'Index__card') and descendant::p[contains(@class,'card-title')]]")
    LOCATOR_SBIS_ABOUT_BUTTON = (By.XPATH, ".//a[@href='/about']")
    LOCATOR_SBIS_PHOTO_GRID = (By.XPATH, "//div[./div/h2[text()='Работаем']]/div[@class='s-Grid-container']//img")
    LOCATOR_SBIS_CONTACTS_CITIES = (By.XPATH, "//div[contains(@id, 'city-id')]")
    LOCATOR_SBIS_REGION_CHOOSER = (By.CSS_SELECTOR, ".ml-16 > span:nth-child(1)")
    LOCATOR_SBIS_REGION_PANEL = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel')
    LOCATOR_SBIS_FOOTER = (By.CSS_SELECTOR, '.sbisru-Footer__container')
    LOCATOR_TAB_BUTTONS = (By.CSS_SELECTOR, ".sbis_ru-VerticalTabs__left")
    LOCATOR_DOWNLOADS = (By.XPATH,
                         "//div[contains(@class, 'ws-has-focus') and @name='SwitchableArea' and @tabindex='2']")

class SearchHelper(BasePage):

    def click_on_the_banner(self):
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_TENSOR_BANNER, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(SbisSearchLocators.LOCATOR_SBIS_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def get_all_info_blocks(self):
        return self.find_elements(SbisSearchLocators.LOCATOR_SBIS_BLOCKS, time=5)

    def get_photos(self):
        return self.find_elements(SbisSearchLocators.LOCATOR_SBIS_PHOTO_GRID, time=2)

    def get_city_names(self):
        return self.find_elements(SbisSearchLocators.LOCATOR_SBIS_CONTACTS_CITIES, time=2)

    def open_region_chooser(self):
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_REGION_CHOOSER, time=2).click()

    def get_region_chooser_panel(self):
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_REGION_PANEL, time=2)

    def get_footer(self):
        return self.find_element(SbisSearchLocators.LOCATOR_SBIS_FOOTER, time=2)

    def tab_buttons(self):
        return self.find_element(SbisSearchLocators.LOCATOR_TAB_BUTTONS, time=2)

    def list_of_downloads(self):
        return self.find_element(SbisSearchLocators.LOCATOR_DOWNLOADS, time=2)


