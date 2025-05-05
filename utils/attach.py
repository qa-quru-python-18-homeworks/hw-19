import allure
import requests

from utils.settings import settings


def attach_bs_video(browser):
    session_id = browser.driver.session_id

    bs_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(settings.bs_username, settings.bs_access_key),
    ).json()
    video_url = bs_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='Screencast',
        attachment_type=allure.attachment_type.HTML,
    )
