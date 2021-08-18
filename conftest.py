from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose laguage:")
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    lang = None
    
    if language_name == "ru":
        print("russian")
        lang = "ru"
    elif language_name == "en":
        print("eng")
        lang = "eng"
    else:
        raise pytest.UsageError("--laguage should be en or ru")
        
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()