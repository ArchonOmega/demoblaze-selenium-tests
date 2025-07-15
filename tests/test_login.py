from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Wait until the login button is visible
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login2")))

    # Use JavaScript to bypass click interception
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(2)

    driver.find_element(By.ID, "loginusername").send_keys("testuserkill")
    driver.find_element(By.ID, "loginpassword").send_keys("testpasskill")
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    time.sleep(5)

    assert "Welcome" in driver.page_source
    driver.quit()
