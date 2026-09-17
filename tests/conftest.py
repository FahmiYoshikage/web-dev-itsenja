import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

BASE_URL = os.environ.get("TEST_BASE_URL", "http://127.0.0.1:8080")
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="function")
def driver():
    """Provides a fresh headless Chrome instance for each E2E test."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1440,900")
    # Suppress console noise
    options.add_argument("--log-level=3")

    service = Service(CHROMEDRIVER_PATH)
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(5)
    
    yield driver_instance
    
    driver_instance.quit()
