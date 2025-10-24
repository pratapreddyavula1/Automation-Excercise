import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import Readconfig


@pytest.fixture(scope="session")
def setup():
    """Fixture to initialize WebDriver and quit after test."""
    popup = webdriver.ChromeOptions()
    popup.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=popup)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Readconfig.getURL())

    yield driver   # ✅ Send driver to the test

    print("\nClosing browser...")
    driver.quit()  # ✅ Proper teardown
