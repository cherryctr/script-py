import os
import time  # Import the time module
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
chrome_driver_path = "C:\\Users\\Admin\\Documents\\pysc\\packages\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Folder to save images
output_folder = "web_design_mockup_images"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Search query for web design mockup images
search_query = "web design mockup"

# Navigate to Google Images search page
url = f"https://www.google.com/search?q={search_query}&tbm=isch"
driver.get(url)
time.sleep(5)  # Let the page load completely

# Scroll down to load more images
for _ in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)

# Get page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
images = soup.find_all('img', {'class': 't0fcAb'})  # Find all images with specific class

# Process each image
for i, img in enumerate(images):
    src = img.get('src')
    if src:
        try:
            response = requests.get(src, stream=True, timeout=10)  # Add timeout parameter
            if response.status_code == 200:
                file_path = os.path.join(output_folder, f'image_{i}.jpg')  # Save as jpg by default
                # Check if the image format is one of the specified formats
                if src.lower().endswith(('.png', '.svg', '.jpeg')):
                    file_path = file_path[:-3] + src.split('.')[-1]  # Change file extension accordingly
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f'Downloaded {src}')
        except Exception as e:
            print(f'Failed to download {src}. Reason: {e}')

# Close the driver
driver.quit()
print('Completed downloading images.')
