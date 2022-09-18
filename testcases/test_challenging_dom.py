import allure
import pytest

from pages.challenging_dom_page import ChallengingDomPage


@allure.parent_suite("Challenge")
@allure.suite("Challenging DOM")
@allure.severity(allure.severity_level.NORMAL)
class TestChallengingDom:

    @pytest.fixture
    def load_page(self, driver, base_url, wait_time):
        self.page = ChallengingDomPage(driver, base_url, wait_time)
        self.page.go_to_challenging_dom_page()

    @allure.description("Page title is displayed")
    @allure.title("Page title is displayed")
    @pytest.mark.nondestructive
    def test_page_title(self, driver, load_page):
        assert self.page.page_title() == 'Challenging DOM'

    @allure.description("All buttons are displayed")
    @allure.title("All buttons are displayed")
    @pytest.mark.nondestructive
    def test_all_buttons_are_displayed(self, driver, load_page):
        assert self.page.buttons_count() == 3
        assert self.page.green_button_is_displayed()
        assert self.page.blue_button_is_displayed()
        assert self.page.red_button_is_displayed()

    @allure.description("Canvas is displayed")
    @allure.title("Canvas is displayed")
    @pytest.mark.nondestructive
    def test_canvas_is_displayed(self, driver, load_page):
        assert self.page.canvas_is_displayed()

    @allure.description("Clicking blue button changes canvas")
    @allure.title("Clicking blue button changes canvas")
    @pytest.mark.nondestructive
    def test_clicking_blue_button_changes_canvas(self, driver, load_page):
        canvas_before = self.page.canvas()
        self.page.click_blue_button()
        canvas_after = self.page.canvas()
        with allure.step("Verifying if canvas has changed"):
            assert not canvas_before == canvas_after

    @allure.description("All columns are displayed")
    @allure.title("All columns are displayed")
    @pytest.mark.nondestructive
    def test_all_table_columns_are_displayed(self, driver, load_page):
        expected_columns = ['Lorem', 'Ipsum', 'Dolor', 'Sit', 'Amet', 'Diceret', 'Action']
        with allure.step(f"Verifying if expected columns displayed: {expected_columns}"):
            assert self.page.table_columns() == expected_columns

    @allure.description("Delete row from table")
    @allure.title("Delete row from table")
    @pytest.mark.nondestructive
    def test_delete_row(self, driver, load_page):
        rows_initial_count = 10
        assert self.page.table_rows_count() == rows_initial_count
        delete_row = self.page.table_rows(1)
        self.page.delete_table_row(1)
        assert delete_row not in self.page.table_rows()
        assert self.page.table_rows_count() == rows_initial_count - 1
