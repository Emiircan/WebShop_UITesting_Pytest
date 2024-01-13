from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield

    driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Automation Report"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    report_file = Path('reports', now.strftime('%d-%m-%Y'))
    report_file.mkdir(parents=True, exist_ok=True)

    report = report_file / f"report_{now.strftime('%H-%M')}.html"
    config.option.htmlpath = report
    config.option.self_contained_html = True
