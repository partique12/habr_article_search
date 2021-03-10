from pylenium.driver import Pylenium
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, py: Pylenium):
        self.py = py

    def search_click(self):
        self.py.get('#search-form-btn').click()

    def search_query(self, query: str):
        self.py.get("#search-form-field").type(query, Keys.ENTER)