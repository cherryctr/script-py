from selenium import webdriver
from selenium.webdriver.common.by import By  # Add this import
import time
import requests
from selenium.webdriver.common.keys import Keys  # Add this import

import os

# Initialize WebDriver (use Chrome or another browser)
driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Documents\\pysc\\packages\\chromedriver.exe")

# Open Google Images
driver.get('https://www.google.com/imghp')

# Enter search keyword
search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search_box.send_keys('cats', Keys.ENTER)  # Replace with the desired search keyword

# # Click the search button
# search_button = driver.find_element(By.XPATH ,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[1]/divs')
# search_button.click()

# Scroll the web page to collect image URLs
scroll_pause_time = 1  # Time pause between each scroll
num_scrolls = 10  # Number of scrolls
img_urls = []

for _ in range(num_scrolls):
    # Scroll down
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(scroll_pause_time)
      
    # Collect image URLs
    img_elements = driver.find_elements(By.XPATH,'//*[@id="dimg_27"]')
    for img_element in img_elements:
        src = img_element.get_attribute('src')
        if src:
            img_urls.append(src)
            if len(img_urls) >= 5000:
                break
    if len(img_urls) >= 5000:
        break

# Create a folder to save images
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# Download images from the collected URLs
for i, img_url in enumerate(img_urls[:5000]):
    try:
        response = requests.get(img_url)
        with open(os.path.join(output_folder, f'image_{i+1}.jpg'), 'wb') as f:
            f.write(response.content)
        print(f'Image {i+1} downloaded successfully')
    except Exception as e:
        print(f'Error downloading image {i+1}: {e}')

# Close the WebDriver
driver.quit()