import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()
    elif browser=='edge':
        driver=webdriver.Edge()
    else:
        options=webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)

    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    driver.maximize_window()
    yield driver
    driver.quit()
