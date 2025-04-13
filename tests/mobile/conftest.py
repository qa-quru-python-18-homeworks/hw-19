import os

import pytest
from appium.options.android import UiAutomator2Options
from selene import browser

from utils.config import Config


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
            "sessionName": "BStack first_test",

            "userName": Config.BS_USERNAME,
            "accessKey": Config.BS_ACCESS_KEY
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('TIMEOUT', '10.0'))

    yield

    browser.quit()
