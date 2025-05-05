import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser

from utils.attach import attach_bs_video
from utils.settings import settings


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Mobile test project",
            "buildName": "browserstack-build",
            "sessionName": "Mobile test",

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

    attach_bs_video(browser)

    browser.quit()
