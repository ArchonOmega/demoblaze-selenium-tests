from selenium.webdriver.common.by import By
import time

def test_signup_modal(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)
    modal_visible = driver.find_element(By.ID, "signInModal").is_displayed()
    assert modal_visible is True
