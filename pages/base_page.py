from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, wait_time):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, wait_time)

    def go_to(self, url):
        self._driver.get(url)

    def elements_count(self, web_element):
        element = self._wait.until(expected_conditions.visibility_of_all_elements_located(web_element))
        return len(element)

    def is_displayed(self, web_element):
        element = self._wait.until(expected_conditions.presence_of_element_located(web_element))
        try:
            return element.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def click(self, web_element):
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.click()

    def fill_text(self, web_element, txt):
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.clear()
        element.send_keys(txt)

    def clear_text(self, web_element):
        element = self._wait.until(expected_conditions.element_to_be_clickable(web_element))
        element.clear()

    def element_text(self, web_element):
        element = self._wait.until(expected_conditions.visibility_of_element_located(web_element))
        return element.text

    def elements_text(self, web_element):
        elements = self._wait.until(expected_conditions.visibility_of_all_elements_located(web_element))
        return [element.text for element in elements]

    def rows(self, web_element):
        return self._wait.until(expected_conditions.visibility_of_all_elements_located(web_element))

    def row_action(self, web_element, index: int):
        self.rows(web_element)[index].click()

    def wait_until_page_loaded(self):
        old_page = self._driver.find_element_by_tag_name('html')
        yield
        self._wait.until(expected_conditions.staleness_of(old_page))

    def get_canvas_png_as_string(self, web_element):
        element = self._wait.until(expected_conditions.visibility_of_element_located(web_element))
        return self._driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);",
            element
        )
