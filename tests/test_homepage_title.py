def test_homepage_title(driver):
    driver.get("https://www.demoblaze.com/")
    assert "STORE" in driver.title
