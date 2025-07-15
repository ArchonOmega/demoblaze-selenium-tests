from selenium.webdriver.common.by import By

def test_unreal_button(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "this_button_does_not_exist").click()  # This will raise NoSuchElementException
