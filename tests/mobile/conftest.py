import uuid

import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser

from utils.settings import settings


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Python project",
            "buildName": "browserstack-build-1",
            "sessionName": str(uuid.uuid4()),

            "userName": settings.bs_username,
            "accessKey": settings.bs_access_key
        }
    })

    browser.config.driver = webdriver.Remote(
        command_executor=settings.bs_url,
        options=options
    )

    browser.config.timeout = settings.timeout

    yield

    browser.quit()
