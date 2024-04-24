from tqdm import tqdm  # Import tqdm for the loading indicator
import requests
import os
import logging
from bs4 import BeautifulSoup
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# Configure logging
logging.basicConfig(filename='image_scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Function to fetch images from a URL
def fetch_images(url, max_images=5):
    image_urls = []
    page = 1
    while len(image_urls) < max_images:
        try:
            response = requests.get(url, params={'page': page})  # Paginate through the search results
            response.raise_for_status()  # Check for any HTTP errors
            soup = BeautifulSoup(response.content, 'html.parser')
            image_tags = soup.find_all('img')
            page_image_urls = [tag['src'] for tag in image_tags]
            image_urls.extend(page_image_urls)
            page += 1
            if not page_image_urls:  # Break if no more images found
                break
        except Exception as e:
            logging.error(f"Error fetching images from URL: {url}, Page: {page}, Error: {e}")
            break
    return image_urls[:max_images]  # Return up to max_images

# Function to save images temporarily and return the file name
def save_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        image = Image.open(BytesIO(response.content))
        file_name = 'temp_image.jpg'  # Save the image temporarily as a JPG file
        # Convert the image to RGB mode for better compatibility
        image = image.convert("RGB")
        # Resize the image to maintain its aspect ratio and improve resolution
        image.thumbnail((800, 800), Image.ANTIALIAS)
        # Ensure that the image resolution is at least 300 pixels per inch (dpi)
        target_resolution = 300
        width, height = image.size
        aspect_ratio = width / height
        new_width = int(target_resolution * aspect_ratio)
        new_height = int(target_resolution)
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image.save(file_name, "JPEG", quality=95)  # Save the image with high quality
        return file_name
    except Exception as e:
        logging.error(f"Error saving image from URL: {url}, Error: {e}")
        return None

# Function to create a PDF and insert the image into it
def create_pdf_and_insert_image(image_url, document_name):
    try:
        pdf_canvas = canvas.Canvas(os.path.join("HASIL JAWABAN FIX", document_name + '.pdf'), pagesize=letter)

        # Add the text "Skill Demonstration Answer" above the image
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(100, 750, "Skill Demonstration Answer")

        image_file = save_image(image_url)
        if image_file:
            pdf_canvas.drawImage(image_file, 100, 100, width=400, height=600)  # Insert the image into the PDF
            pdf_canvas.save()
            os.remove(image_file)  # Remove the temporary image file after use
        else:
            logging.error(f"Image file not found for URL: {image_url}")
    except Exception as e:
        logging.error(f"Error creating PDF and inserting image for URL: {image_url}, Error: {e}")

# URLs of websites to fetch images from
urls_website = [
    'https://id.pinterest.com/almarodigital/web-toko-online/',
    'https://id.pinterest.com/search/pins/?rs=ac&len=2&q=ecommerce%20web%20design&eq=ecomm&etslf=9516',
    'https://id.pinterest.com/search/pins/?rs=ac&len=2&q=ecommerce%20website&eq=ecommerce%20we&etslf=3821',
    'https://id.pinterest.com/search/pins/?rs=ac&len=2&q=ecommerce%20web%20design&eq=ecomm&etslf=9516',
    'https://id.pinterest.com/search/pins/?q=ecommerce%20web%20design%20layout&rs=guide&sourceModuleId=OB_ecommerce_web_design_layout_1165a77b-b7be-457d-aba5-3156ba3ad061&journeyDepth=&',
]

# Create output folder if it doesn't exist
output_folder = "HASIL JAWABAN FIX"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Fetch images and create PDF documents
for j, url in enumerate(urls_website):
    try:
        total = 5
        image_urls = fetch_images(url, max_images=total)  # Adjust max_images to 1000
        for i, image_url in enumerate(tqdm(image_urls, desc=f"Fetching images from URL {j+1}")):
            document_name = f'TUGAS_{i+1}'  # Modify the document name
            create_pdf_and_insert_image(image_url, document_name)
    except Exception as e:
        logging.error(f"Error processing URL: {url}, Error: {e}")

logging.info("Image scraping process completed.")
