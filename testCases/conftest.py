from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path="C://Users//ayussriv//Downloads//geckodriver-v0.30.0-win64 (1)//geckodriver.exe")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####### Pytest html report ########################

# This metadata used for adding customised environment data
def pytest_configure(config):
    config._metadata['Project Name'] = "nop commerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = "Ayush Srivastava"

# This hook will delete/modify the unnecessary data from reports

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
