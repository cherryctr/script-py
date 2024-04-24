import requests
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
chromedriver_path = "C:\\Users\\MSI Thin\\Documents\\chrry\\script\\script-py\\packages\\chromedriver.exe"

# Configure headless Chrome for faster performance
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# Daftar URL yang akan diambil screenshot
urls = [
    "https://www.tokopedia.com/zunairamuslimah",
    "https://www.tokopedia.com/pickipee",
    ...
]

# Fungsi untuk mengambil screenshot dari URL dan menyimpannya dalam file PDF
def take_screenshot_to_pdf(url, filename):
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Screenshot: " + url, ln=True, align="C")
    pdf.image(image=screenshot, x=10, y=30, w=180)  # Adjust x, y, w as needed
    pdf.output(filename)
    
    print("Screenshot dari", url, "telah disimpan sebagai", filename)
    
    # Optional: Delete temporary screenshot file (if needed)
    # os.remove("screenshot.png")

# Loop untuk mengambil screenshot dari setiap URL
for i, url in enumerate(urls):
    filename = f"jawaban_{i+1}.pdf"
    take_screenshot_to_pdf(url, filename)
