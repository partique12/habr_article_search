def test_search(py, habr):
    habr.goto()
    habr.home.search_click()
    habr.home.search_query('системный подход к личности')
    habr.srp.open_article()

    assert py.contains('Системный подход к личности')
