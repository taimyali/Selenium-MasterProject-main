from selenium import webdriver # Importing the webdriver to control the browser
from selenium.webdriver.chrome.service import Service # Importing the Service class to manage the ChromeDriver service
from selenium.webdriver.common.keys import Keys # Importing Keys to simulate keyboard actions like entering text
import pandas as pd # Importing pandas for data manipulation and saving data to CSV
import time # Importing time to add delays in the script
from selenium.webdriver.support import expected_conditions as EC # Importing expected_conditions to wait for certain conditions in the browser
from selenium.webdriver.support.ui import WebDriverWait # Importing WebDriverWait to wait for certain conditions to be met before proceeding
from selenium.webdriver.common.by import By # Importing By to locate elements on the page
from selenium.webdriver.chrome.options import Options # Importing Options to set ChromeDriver options

path = r'C:\Selenium Drivers\chromedriver-win64\chromedriver.exe' # Path to the ChromeDriver executable

service = Service(path) # Creating a Service object with the path to the ChromeDriver executable
service.start() # Starting the ChromeDriver service

# Headless mode
options = Options()  # Initialize an instance of the Options class
options.headless = True  # True -> Headless mode activated

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

# Finding the last page of the pagination bar
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

# Initializing storage
book_title = []
book_author = []
book_length = []
current_page = 1

# The while loop below will work until the the bot reaches the last page of the website, then it will break
while current_page <= last_page:
    # Implicit Wait
    time.sleep(2)
    # Explicit Wait
    # container = driver.find_element_by_class_name('adbl-impression-container ')
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
    # products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))

    # Looping through the products list (each "product" is an audiobook)
    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

    # Increment the current_page by 1 after the data is extracted
    current_page = current_page + 1

    # Locating the next_page button and clicking on it. If the element isn't on the website, pass to the next iteration
    try:
        next_page = driver.find_element_by_xpath('.//span[contains(@class , "nextButton")]')
        next_page.click()
    except:
        pass

# Closing the browser
driver.quit()

# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_pagination.csv', index=False)
