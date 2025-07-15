import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    yield driver
    # This executes after the test runs
    outcome = request.node.__dict__.get("test_outcome", None)
    if outcome and outcome.failed:
        screenshot_name = f"screenshots/{request.node.name}.png"
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
