from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/contacts"
        self.actions = ActionChains(self.driver)

    def scroll_to_the_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_elusive_element(self, element):
        return self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20)
                                          .until(EC.element_to_be_clickable(element)))

    def hover_over(self, element):
        return self.actions.move_to_element(element).perform()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_tab(self):
        chwd = self.driver.window_handles
        if len(chwd) > 1:
            return self.driver.switch_to.window(chwd[1])

    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title





