import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_webdriver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver


@pytest.fixture()
def set_window_size():
    browser.config.window_width = 1080
    browser.config.window_height = 920


@pytest.fixture()
def open_browser(set_webdriver, set_window_size):
    browser.open('https://google.com/ncr')
