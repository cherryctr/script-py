import os
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Configure logging
logging.basicConfig(filename='screenshot_scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def read_urls_from_excel(file_path, sheet_name=0, column='URL'):
    """
    Function to read URLs from an Excel file in a specific column.

    Args:
    - file_path (str): Path to the Excel file.
    - sheet_name (str or int, optional): Name or index of the sheet to read from. Defaults to 0.
    - column (str, optional): Column name or index to read URLs from. Defaults to 'URL'.

    Returns:
    - urls (list): List of URLs extracted from the specified column.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        urls = df[column].tolist()
        return urls
    except Exception as e:
        logging.error(f"Failed to read URLs from Excel file: {e}")
        return []

def create_pdf_from_screenshot(html_file, pdf_file):
    try:
        # Set up Selenium Chrome driver
        chrome_options = Options()
        chrome_options.headless = True
        service = Service(r"C:\Users\Admin\Documents\pysc\excels\web_link1.xlsx")  # Set the path to your chromedriver executable
        service.start()
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Open the HTML file in Chrome
        driver.get('file://' + os.path.abspath(html_file))

        # Take screenshot
        screenshot_file = 'screenshot.png'
        driver.save_screenshot(screenshot_file)

        # Close the Chrome driver
        driver.quit()

        # Create PDF and insert screenshot
        pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)
        pdf_canvas.drawImage(screenshot_file, 0, 0, width=letter[0], height=letter[1])
        pdf_canvas.save()

        # Delete temporary files
        os.remove(screenshot_file)
    except Exception as e:
        logging.error(f"Error creating PDF from screenshot: {e}")

def process_html_files_from_excel(excel_path):
    try:
        html_files = read_urls_from_excel(excel_path)
        for i, html_file in enumerate(html_files):
            if html_file.endswith('.html'):
                document_name = f'Document_{i+1}'
                pdf_file = f"{document_name}.pdf"
                create_pdf_from_screenshot(html_file, pdf_file)
    except Exception as e:
        logging.error(f"Error processing HTML files from Excel: {e}")

if __name__ == "__main__":
    excel_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\web_link1.xlsx"
    process_html_files_from_excel(excel_path)
