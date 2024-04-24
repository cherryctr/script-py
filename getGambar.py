import requests
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
chromedriver_path = 'path/to/chromedriver'

# Configure headless Chrome for faster performance
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Daftar URL yang akan diambil screenshot
urls = [
    "https://www.tokopedia.com/zunairamuslimah",
    "https://www.tokopedia.com/pickipee",
    "https://www.tokopedia.com/ghaniastudio",
    "https://www.tokopedia.com/argyahi",
    "https://www.tokopedia.com/salenahijab",
    "https://www.tokopedia.com/archive-bundaawa",
    "https://www.tokopedia.com/rezahijabfashion",
    "https://www.tokopedia.com/vatira",
    "https://www.tokopedia.com/hilawah-hijab",
    "https://www.tokopedia.com/dailyhijabsuhaila",
    "https://www.tokopedia.com/ayurihijab",
    "https://www.tokopedia.com/lathiifshoping",
    "https://www.tokopedia.com/morohelm",
    "https://www.tokopedia.com/whiezha",
    "https://www.tokopedia.com/ayanahijabshop",
    "https://www.tokopedia.com/myhijabonlineshop",
    "https://www.tokopedia.com/isya-hijab",
    "https://www.tokopedia.com/zoha-hijab",
    "https://www.tokopedia.com/r-l-hijab-1",
    "https://www.tokopedia.com/vigoeshop",
