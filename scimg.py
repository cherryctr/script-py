import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def download_images(search_term, num_images=10, output_folder="sample_data", driver_path="C:\\Users\\Admin\\Documents\\pysc\\packages\\chromedriver.exe"):
    # Initialize the Chrome WebDriver service
    service = Service(driver_path)

    # Initialize Chrome driver with the specified service
    driver = webdriver.Chrome(service=service)

    # Google Image Search URL template
    url = "https://www.google.com/search?q={}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"

    # Load the Google Image Search page with the specified search term
    driver.get(url.format(search_term))

    # Scroll down to load more images
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    # Wait for page to load images
    time.sleep(2)

    # Find all image elements using full XPath
    img_results = driver.find_elements(By.XPATH, "/html/body/div[5]/div/div[13]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[2]/h3/a/div/div/div/g-img/img")

    img_src = []

    # Extract image URLs
    for img in img_results:
        src = img.get_attribute('src')
        if src:
            img_src.append(src)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Limit the number of images to download to the minimum between the specified number and the actual number of images found
    num_images_to_download = min(len(img_src), num_images)

    # Download images
    for i in range(num_images_to_download):
        try:
            img_url = img_src[i]
            filename = f"{output_folder}/{search_term}{i}.jpg"
            urllib.request.urlretrieve(img_url, filename)
            print(f"Downloaded image {i+1}/{num_images_to_download}: {img_url}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")

    # Close the browser
    driver.quit()

# Example usage:
download_images("pets", num_images=10, output_folder="sample_data")
