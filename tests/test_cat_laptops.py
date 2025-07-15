from selenium.webdriver.common.by import By
import time

def test_cat_laptops(driver):
    driver.get("https://www.demoblaze.com/")
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(2)
    assert "Laptops" in driver.page_source
