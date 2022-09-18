import json

import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


CONFIG_PATH = "testcases/config.json"


@pytest.fixture(scope="session")
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def wait_time(config):
    return config['wait_time']


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store", default=False)


@pytest.fixture(autouse=True, scope="class")
def driver(request):
    browser = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise Exception("Incorrect Browser")

    driver.maximize_window()

    yield driver

    if driver is not None:
        driver.close()
        driver.quit()
