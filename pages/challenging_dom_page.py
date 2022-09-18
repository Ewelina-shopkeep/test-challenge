import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ChallengingDomPage(BasePage):
    def __init__(self, driver, base_url, wait_time):
        self.url = base_url+"/challenging_dom"
        super().__init__(driver, wait_time)

    BUTTONS = (By.CLASS_NAME, "button")
    BUTTON_BLUE = (By.CLASS_NAME, "button:not(.alert):not(.success)")
    BUTTON_RED = (By.CLASS_NAME, "button.alert")
    BUTTON_GREEN = (By.CLASS_NAME, "button.success")
    CANVAS = (By.ID, "canvas")
    TABLE_COLUMNS = (By.CSS_SELECTOR, "thead th")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody tr")
    EDIT_BUTTON = (By.LINK_TEXT, "edit")
    DELETE_BUTTON = (By.LINK_TEXT, "delete")
    PAGE_TITLE = (By.TAG_NAME, "h3")

    @allure.step("Navigating to Challenging DOM page")
    def go_to_challenging_dom_page(self):
        self.go_to(self.url)

    @allure.step("Verifying if canvas is displayed")
    def canvas_is_displayed(self):
        return self.is_displayed(self.CANVAS)

    @allure.step("Verifying if blue button is displayed")
    def blue_button_is_displayed(self):
        return self.is_displayed(self.BUTTON_BLUE)

    @allure.step("Clicking blue button")
    def click_blue_button(self):
        self.click(self.BUTTON_BLUE)

    @allure.step("Verifying if green button is displayed")
    def green_button_is_displayed(self):
        return self.is_displayed(self.BUTTON_GREEN)

    @allure.step("Clicking green button")
    def click_green_button(self):
        self.click(self.BUTTON_GREEN)

    @allure.step("Verifying if red button is displayed")
    def red_button_is_displayed(self):
        return self.is_displayed(self.BUTTON_RED)

    @allure.step("Clicking red button")
    def click_red_button(self):
        self.click(self.BUTTON_RED)

    @allure.step("Getting page title")
    def page_title(self):
        return self.element_text(self.PAGE_TITLE)

    def canvas(self):
        return self.get_canvas_png_as_string(self.CANVAS)

    @allure.step("Getting count od displayed buttons")
    def buttons_count(self):
        return self.elements_count(self.BUTTONS)

    @allure.step("Getting displayed columns names")
    def table_columns(self):
        return self.elements_text(self.TABLE_COLUMNS)

    @allure.step("Getting table rows count")
    def table_rows_count(self):
        return self.elements_count(self.TABLE_ROWS)

    @allure.step("Getting table rows count")
    def table_rows(self, index: int = None):
        if index:
            return self.rows(self.TABLE_ROWS)[index]
        else:
            return self.rows(self.TABLE_ROWS)

    @allure.step("Deleting table row")
    def delete_table_row(self, index: int):
        return self.row_action(self.DELETE_BUTTON, index)

    @allure.step("Editing table row")
    def edit_table_row(self, index: int):
        return self.row_action(self.EDIT_BUTTON, index)
