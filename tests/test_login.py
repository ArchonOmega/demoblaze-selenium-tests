from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Wait for the login button to be clickable and scroll it into view
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
    driver.execute_script("arguments[0].scrollIntoView();", login_button)
    login_button.click()
    time.sleep(2)

    # Fill login form
    driver.find_element(By.ID, "loginusername").send_keys("testuserkill")
    driver.find_element(By.ID, "loginpassword").send_keys("testpasskill")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    time.sleep(5)

    # Verify login attempt (can be adjusted based on actual success message)
    assert "Welcome" in driver.page_source
    driver.quit()
