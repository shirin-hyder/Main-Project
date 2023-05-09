import requests
from bs4 import BeautifulSoup
import cloudscraper
scraper = cloudscraper.create_scraper()

# Get user input for job keywords and location
keywords = input("Enter job keywords: ")
location = input("Enter job location: ")

# Build URL for job search with keywords and location
url = f"https://in.indeed.com/jobs?q={keywords}&l={location}"

# Send GET request to URL and parse HTML with BeautifulSoup
response = scraper.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
# Find all job listings on the page
job_listings = soup.find_all(class_="mosaic-provider-jobcards")
print(job_listings)

# Print the title, company, and location for each job listing
# for job in job_listings:
#     title = job.find(class_="title").text.strip()
#     company = job.find(class_="company").text.strip()
#     location_elem = job.find(class_="location")
#     location = location_elem.text.strip() if location_elem else "N/A"
#     print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")
for job in job_listings:
    try:
        title = job.find(class_="jcs-JobTitle").text.strip()
        company = job.find(class_="companyName").text.strip()
        location_elem = job.find(class_="location")
        location = location_elem.text.strip() if location_elem else "N/A"
        print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")
    except AttributeError:
        print("Error: could not find job information")



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Get user input for job keywords and location
# keywords = input("Enter job keywords: ")
# location = input("Enter job location: ")

# # Set up Chrome webdriver with Selenium
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

# # Build URL for job search with keywords and location
# # url = f"https://www.indeed.com/jobs?q={keywords}&l={location}"
# url = f"https://www.naukri.com/{keywords}-freshers-jobs-in-{location}"

# # Navigate to the URL and wait for the page to load
# driver.get(url)
# wait.until(EC.presence_of_element_located((By.ID, "resultsCol")))

# # Parse HTML with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # Find all job listings on the page
# job_listings = soup.find_all(class_="jobsearch-SerpJobCard")
# print(job_listings)

# # Print the title, company, and location for each job listing
# for job in job_listings:
#     title = job.find(class_="title").text.strip()
#     company = job.find(class_="company").text.strip()
#     location = job.find(class_="location").text.strip()
#     print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")

# # Close the webdriver
# driver.quit()
