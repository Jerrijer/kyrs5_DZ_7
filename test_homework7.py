import os
import csv
import zipfile

from pypdf import PdfReader
import xlrd
from openpyxl import load_workbook
import time
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file_with_browser():
    project_root_path = os.path.dirname(os.path.abspath(__file__))
    path_browser = os.path.join(project_root_path, 'resources')

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": path_browser,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options


    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(3)


    assert os.path.exists(os.path.join(path_browser, 'pytest-main.zip'))
    assert os.path.getsize(os.path.join(path_browser, 'pytest-main.zip')) > 0

