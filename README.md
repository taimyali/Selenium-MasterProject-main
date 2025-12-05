# Selenium-MasterProject-main
This repository demonstrates how to scrape the Audible website using Selenium with pagination and a custom bot. Follow the steps below to set up and run the project smoothly on both Windows and macOS. Instructions are provided for both .ipynb and .py file users.
Prerequisites
Python Installation
Ensure Python 3.7 or above is installed on your system. You can download it from python.org.

Google Chrome Installation
Install the latest version of Google Chrome from google.com/chrome.

ChromeDriver Installation

Download the ChromeDriver version compatible with your Chrome browser from chromedriver.chromium.org.
Windows: Extract the chromedriver.exe file and place it in a known directory (e.g., C:\chromedriver\chromedriver.exe).
macOS: Extract the chromedriver file and move it to /usr/local/bin/ or another directory in your PATH.
Install Required Libraries
Install the necessary Python libraries using the requirements.txt file:

pip install -r requirements.txt
Project Setup
Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/MuhammadUzair1/Selenium-MasterProject
cd Selenium-MasterProject
Update the ChromeDriver Path
Update the path variable in the script to point to your ChromeDriver location:

path = '/path/to/chromedriver'  # Replace with your actual path
Run the Script

For .py Users:
Run the script using the command:
python script.py
For .ipynb Users:
Open the Jupyter Notebook and run the cells sequentially:
jupyter notebook script.ipynb
Audible Website to Scrape
The script scrapes data from the following Audible page:

Audible Best Sellers
Output
The script extracts the following data:

Book Title
Book Author
Book Length
The data is saved in a CSV file named books_pagination.csv in the project directory.

Notes
Ensure your ChromeDriver version matches your Chrome browser version.
If you encounter issues with Selenium, verify that the chromedriver executable is in your PATH or update the path variable in the script.
The script uses Selenium 3.141.0. If you wish to use a newer version, update the code accordingly.
Troubleshooting
Common Errors:
WebDriverException: Ensure the ChromeDriver path is correct.
NoSuchElementException: Verify that the website's structure has not changed.
Debugging:
Use time.sleep() to allow pages to load fully.
Check the website's HTML structure using browser developer tools.
Enjoy scraping Audible with this project!
