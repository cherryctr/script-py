import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Path to the Excel file containing the URLs
excel_file_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\index401.xlsx"

# Define the index of the column containing the URLs (assuming it's the second column)
url_column_index = 2
url_column_catatan = 3

# Path to ChromeDriver executable
chrome_driver_path = "C:\\Users\\Admin\\Documents\\pysc\\packages\\chromedriver.exe"

# Create Chrome WebDriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")  # Disable notifications
try:
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
except Exception as e:
    print("Error creating Chrome WebDriver:", e)
    exit()

# Load the Excel workbook
workbook = openpyxl.load_workbook(excel_file_path)

# Get the active worksheet
worksheet = workbook.active

# Iterate through each row in Excel data
for row_num, row in enumerate(worksheet.iter_rows(min_row=2, max_col=2, values_only=True), start=2):  # Start from the second row
    url = row[url_column_index - 1]  # Adjust index to 0-based

    if not url:
        continue

    try:
        driver.get(url)
        print("Opened URL:", url)

        # Using find_element() with By.ID
        tbody_encounter_list = None
        try:
            tbody_encounter_list = driver.find_element(By.ID, "encounterList")
        except NoSuchElementException:
            pass

        if tbody_encounter_list:
            tr_elements = tbody_encounter_list.find_elements(By.TAG_NAME, "tr")
            td_elements = tbody_encounter_list.find_elements(By.TAG_NAME, "td")
            if tr_elements and td_elements:
                if "Post Test" in driver.page_source:
                    worksheet.cell(row=row_num, column=url_column_catatan, value="Belum Rating")
                    print("Updated 'Catatan' column with: Belum Rating")
                else:
                    worksheet.cell(row=row_num, column=url_column_catatan, value="Belum Selesai")
                    print("Updated 'Catatan' column with: Belum Selesai")
            else:
                worksheet.cell(row=row_num, column=url_column_catatan, value="Error")
                print("Updated 'Catatan' column with: Error")
        else:
            worksheet.cell(row=row_num, column=url_column_catatan, value="Error")
            print("Updated 'Catatan' column with: Error")

    except Exception as e:
        print("Error processing URL:", url, "-", e)

# Save and close operations
excel_export_path = "C:\\Users\\Admin\\Documents\\pysc\\excels\\index401_result.xlsx"
# Check if the export file already exists
export_file_exists = True
export_file_counter = 1
while export_file_exists:
    try:
        workbook.save(excel_export_path)
        export_file_exists = False
    except PermissionError:
        export_file_counter += 1
        excel_export_path = f"C:\\Users\\Admin\\Documents\\pysc\\excels\\index401_result_{export_file_counter}.xlsx"

print("Exported data to:", excel_export_path)

driver.quit()
workbook.close()
