import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Constants

DUCKDUCKGO_HOME = 'http://duckduckgo.com/'

#Scenarios

scenarios('../features/web.feature')

#Fixtures

@pytest.fixture(scope="class")
def browser(request):
    #For this example, we will use Firefox
    #You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)

#When Steps
@when(parsers.parse('the user searches for "{text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element(By.NAME, "q")
    search_input.send_keys(text+ Keys.RETURN)