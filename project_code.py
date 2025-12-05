from selenium import webdriver # Importing the webdriver to control the browser
from selenium.webdriver.chrome.service import Service # Importing the Service class to manage the ChromeDriver service
from selenium.webdriver.common.keys import Keys # Importing Keys to simulate keyboard actions like entering text
import pandas as pd # Importing pandas for data manipulation and saving data to CSV
import time # Importing time to add delays in the script
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

path = r'C:\Selenium Drivers\chromedriver-win64\chromedriver.exe'

service = Service(path) # Creating a Service object with the path to the ChromeDriver executable
service.start() # Starting the ChromeDriver service

driver = webdriver.Chrome(path) # Creating a Chrome WebDriver instance
driver.get("https://www.audible.com/search") # Navigating to the Audible search page
driver.maximize_window()

# selecting English checkbox for the language filter
checkboxes = driver.find_elements_by_xpath("//span[@class='bc-checkbox-label bc-size-callout']") # Getting the text of the checkbox element

# Wait until the visible clickable area is available
checkbox_fake_area = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH, "//span[contains(@class, 'bc-checkbox-label') and contains(text(), 'English')]"
    ))
)

# Click the visible label "English" to select checkbox
checkbox_fake_area.click() # Clicking the checkbox to select it

# Locating the box that contains all the audiobooks listed in the page
container = driver.find_element_by_class_name('adbl-impression-container ')

# Getting all the audiobooks listed (the "/" gives immediate child nodes)
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')
# products = container.find_elements_by_xpath('./li')

# Initializing storage
book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)  # Storing data in list
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)

