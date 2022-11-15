def test_hello_world(browser):
    browser.get("https://ya.ru")
    assert "Яндекс" in browser.title
