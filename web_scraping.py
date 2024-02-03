import requests
from bs4 import BeautifulSoup

# 1. Making a request to a website
url = 'https://example.com'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code: {response.status_code}")
    exit()

# 2. Parsing the HTML content
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

# 3. Extracting data using BeautifulSoup
# Example: Extracting all links (anchor tags)
all_links = soup.find_all('a')

print("All Links:")
for link in all_links:
    print(link.get('href'))

# 4. Extracting specific data
# Example: Extracting the title of the page
title = soup.title.string
print(f"Title of the Page: {title}")

# 5. Navigating the HTML tree
# Example: Extracting the text of the first paragraph
first_paragraph = soup.p.text
print(f"First Paragraph: {first_paragraph}")

# 6. Scraping multiple pages
# Example: Scraping a list of pages
for page_number in range(1, 4):
    page_url = f'https://example.com/page/{page_number}'
    page_response = requests.get(page_url)

    if page_response.status_code == 200:
        page_soup = BeautifulSoup(page_response.content, 'html.parser')
        # Perform scraping for each page as needed

# Note: Web scraping is subject to change as websites evolve. Be sure to adapt your code accordingly.
# Additionally, consider using APIs if available and respecting the website's terms of service.
# This example uses the requests library to make HTTP requests and BeautifulSoup for parsing HTML content. 
# The comments provide explanations for each section. 
# Remember to install the required libraries using: pip install requests beautifulsoup4
