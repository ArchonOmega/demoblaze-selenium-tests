import pytest

@pytest.mark.xfail(reason="Testing title assertion failure")
def test_wrong_hp_title(driver):
    driver.get("https://www.demoblaze.com/")
    assert "Not The Store" in driver.title  # This will fail
