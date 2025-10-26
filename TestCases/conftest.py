import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Utilities.readProperties import Readconfig

# ✅ Add CLI option to specify browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name: chrome, firefox, or edge")

@pytest.fixture(scope="session")
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=Service("C:\\Users\\prata\\Downloads\\edgedriver_win64 (3)\\msedgedriver.exe"), options=options)

    else:
        raise ValueError(f"❌ Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Readconfig.getURL())

    yield driver
    driver.quit()

"""Capturing Screenshot when test Fails..."""
@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    rep=outcome.get_result()
    if rep.when=="call" and rep.failed:
        driver=item.funcargs.get("setup")
        if driver:
            SS=os.path.join(os.getcwd(),"ScreenShots")
            os.makedirs(SS,exist_ok=True)

            # File name format
            file_name = f"{rep.nodeid.replace('::', '_').replace('/', '_')}.png"
            destination = os.path.join(SS, file_name)

            # Take screenshot
            driver.save_screenshot(destination)
            print(f"\n📸 Screenshot saved at: {destination}")

            # ✅ If using Allure Report
            try:
                import allure
                with open(destination, "rb") as image_file:
                    allure.attach(image_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
            except ImportError:
                pass

