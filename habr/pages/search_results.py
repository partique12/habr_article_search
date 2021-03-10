from pylenium.driver import Pylenium


class SearchResultsPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def open_article(self):
        self.py.get("#post_545832 h2").click()
