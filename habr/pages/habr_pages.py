from pylenium.driver import Pylenium

from habr.pages.home_page import HomePage
from habr.pages.search_results import SearchResultsPage


class HabrPages:
    def __init__(self, py: Pylenium):
        self.py = py
        self.home = HomePage(py)
        self.srp = SearchResultsPage(py)

    def goto(self) -> Pylenium:
        return self.py.visit('https://habr.com/ru/')
