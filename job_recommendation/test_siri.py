# import requests
# from bs4 import BeautifulSoup
# import cloudscraper
# scraper = cloudscraper.create_scraper()

# # Get user input for job keywords and location
# keywords = input("Enter job keywords: ")
# location = input("Enter job location: ")

# # Build URL for job search with keywords and location
# url = f"https://in.indeed.com/jobs?q={keywords}&l={location}"

# # Send GET request to URL and parse HTML with BeautifulSoup
# response = scraper.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# # Find all job listings on the page
# job_listings = soup.find_all(class_="mosaic-provider-jobcards")
# print(job_listings)

# # Print the title, company, and location for each job listing
# # for job in job_listings:
# #     title = job.find(class_="title").text.strip()
# #     company = job.find(class_="company").text.strip()
# #     location_elem = job.find(class_="location")
# #     location = location_elem.text.strip() if location_elem else "N/A"
# #     print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")
# for job in job_listings:
#     try:
#         title = job.find(class_="jcs-JobTitle").text.strip()
#         company = job.find(class_="companyName").text.strip()
#         location_elem = job.find(class_="location")
#         location = location_elem.text.strip() if location_elem else "N/A"
#         print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")
#     except AttributeError:
#         print("Error: could not find job information")



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


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import nltk
nltk.data.path.append("/home/ashiq/nltk_data")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

# Configure Selenium to use Chrome driver
driver = webdriver.Chrome()

# Get user input for job keywords and location
# keywords = input("Enter job keywords: ")
# location = input("Enter job location: ")
# Get user input for job description
description = input("Enter job description: ")

# Tokenize the description into words
words = word_tokenize(description)

# Remove stop words (common words that don't add meaning)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if not word in stop_words]

# Define a list of Python-related keywords
python_keywords = ['python', 'pytorch', 'sql', 'mxnet', 'mlflow', 'einstein', 'theano', 'pyspark', 'solr', 'mahout', 
 'cassandra', 'aws', 'powerpoint', 'spark', 'pig', 'sas', 'java', 'nosql', 'docker', 'salesforce', 'scala', 'r',
 'c', 'c++', 'net', 'tableau', 'pandas', 'scikitlearn', 'sklearn', 'matlab', 'scala', 'keras', 'tensorflow', 'clojure',
 'caffe', 'scipy', 'numpy', 'matplotlib', 'vba', 'spss', 'linux', 'azure', 'cloud', 'gcp', 'mongodb', 'mysql', 'oracle', 
 'redshift', 'snowflake', 'kafka', 'javascript', 'qlik', 'jupyter', 'perl', 'bigquery', 'unix', 'react',
 'scikit', 'powerbi', 's3', 'ec2', 'lambda', 'ssrs', 'kubernetes', 'hana', 'spacy', 'tf', 'django', 'sagemaker',
 'seaborn', 'mllib', 'github', 'git', 'elasticsearch', 'splunk', 'airflow', 'looker', 'rapidminer', 'birt', 'pentaho', 
 'jquery', 'nodejs', 'd3', 'plotly', 'bokeh', 'xgboost', 'rstudio', 'shiny', 'dash', 'h20', 'h2o', 'hadoop', 'mapreduce', 
 'hive', 'cognos', 'angular', 'nltk', 'flask', 'node', 'firebase', 'bigtable', 'rust', 'php', 'cntk', 'lightgbm', 
 'kubeflow', 'rpython', 'unixlinux', 'postgressql', 'postgresql', 'postgres', 'hbase', 'dask', 'ruby', 'julia', 'tensor',
# added r packages doesn't seem to impact the result
 'dplyr','ggplot2','esquisse','bioconductor','shiny','lubridate','knitr','mlr','quanteda','dt','rcrawler','caret','rmarkdown',
 'leaflet','janitor','ggvis','plotly','rcharts','rbokeh','broom','stringr','magrittr','slidify','rvest',
 'rmysql','rsqlite','prophet','glmnet','text2vec','snowballc','quantmod','rstan','swirl','datasciencer']

# Find keywords in the filtered words
found_keywords = [word for word in filtered_words if word in python_keywords]
keywords = "+".join(found_keywords)
print(found_keywords)
# Get user input for job location
location = input("Enter job location: ")

# Build URL for job search with keywords and location
url = f"https://in.indeed.com/jobs?q={keywords}&l={location}"

# Open URL in Selenium-controlled Chrome browser
driver.get(url)

# Wait for page to load
driver.implicitly_wait(10)

# Scroll down to load more job listings
for i in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    driver.implicitly_wait(2)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")



# Find all job listings on the page
job_listings = soup.find_all(class_="tapItem")

# Print the title, company, and location for each job listing
for job in job_listings:
    try:
        title = job.find(class_=["jobTitle"]).text.strip()
        company = job.find(class_="companyName").text.strip()
        location_elem = job.find(class_="companyLocation")
        location = location_elem.text.strip() if location_elem else "N/A"
        print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n")
    except AttributeError:
        print("Error: could not find job information")
#Close the Selenium-controlled browser
driver.quit()

