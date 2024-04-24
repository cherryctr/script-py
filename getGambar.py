
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
    "https://www.tokopedia.com/barynt",
    "https://www.tokopedia.com/missde",
    "https://www.tokopedia.com/danstoreid11",
    "https://www.tokopedia.com/lovincraft",
    "https://www.tokopedia.com/koshoku",
    "https://www.tokopedia.com/fikriasesories",
    "https://www.tokopedia.com/fashiondisplaymj",
    "https://www.tokopedia.com/lajuh-1",
    "https://www.tokopedia.com/yesbuka",
    "https://www.tokopedia.com/ocmart"
]

# Fungsi untuk mengambil screenshot dari URL dan menyimpannya dalam file PDF
def take_screenshot_to_pdf(url, filename):
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    driver.get(url)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Screenshot: " + url, ln=True, align="C")
    pdf.image(x=10, y=20, w=180, f="PNG", image=screenshot)
    pdf.output(filename)
    
    print("Screenshot dari", url, "telah disimpan sebagai", filename)
    
    # Optional: Delete temporary screenshot file (if needed)
    # os.remove("screenshot.png")

# Loop untuk mengambil screenshot dari setiap URL
for i, url in enumerate(urls):
    filename = f"jawaban_{i+1}.pdf"
    take_screenshot_to_pdf(url, filename)