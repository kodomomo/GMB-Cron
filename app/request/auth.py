from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app.config import (
    chrome_driver_path, OAUTH_URL,
    EMAIL, PASSWORD
)


class AutoLogin:

    def __init__(self):
        self._chrome = Chrome(chrome_driver_path())

    def execute(self):
        self._move_to_page(OAUTH_URL)
        self._write("email", EMAIL)
        self._write("pass", PASSWORD + Keys.RETURN)
        try:
            self._click('back')
            sleep(3)
        except:
            pass

    def _move_to_page(self, url: str):
        self._chrome.get(url)

    def _write(self, scope_id: str, value: str):
        scope = self._get_element_by_id(scope_id)
        scope.send_keys(value)

    def _click(self, scope_id: str):
        scope = self._get_element_by_id(scope_id)
        scope.click()

    def _get_element_by_id(self, scope_id):
        return self._chrome.find_element(by=By.ID, value=scope_id)
