from selenium import webdriver
import time

def test_open_homepage():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)  # Wait for page to load
    assert "STORE" in driver.title
    driver.quit()
