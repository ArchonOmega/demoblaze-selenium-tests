import pytest
import datetime
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome()
    yield driver
    # This executes after the test runs
    outcome = request.node.__dict__.get("test_outcome", None)
    if outcome and outcome.failed:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/{request.node.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved to {screenshot_name}")
    driver.quit()

# Store result in node dict cleanly
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        item.test_outcome = result
