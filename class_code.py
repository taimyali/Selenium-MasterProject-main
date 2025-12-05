from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:\Selenium Drivers\chromedriver-win64\chromedriver.exe'

# Starting the Chrome driver service
ser = Service(path)
ser.start()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(path)
driver.maximize_window()

# Open a website
driver.get('https://www.audible.com/search')

# Selecting English checkbox for the language filter
select_english = driver.find_element_by_xpath("//span[@class='bc-checkbox-label bc-size-callout' and contains(text(),'English')]")
english = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='bc-checkbox-label bc-size-callout' and contains(text(),'English')]"))
)
english.click()

# Getting infromation from the page
separator = driver.find_element_by_xpath("//div[@id='center-3']")
songs = separator.find_elements_by_xpath('.//li[contains(@class, "bc-list-item") and contains(@id, "product-list-item")]')

print("Number of songs: ", len(songs))



driver.quit()  # Close the browser and end the session