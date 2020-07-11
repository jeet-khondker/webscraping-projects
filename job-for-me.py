import requests
from bs4 import BeautifulSoup
import re

query = ''
BASE_URL = "https://www.google.com/search?q="

# List Containing Keyword Terms That Describe My Wanted Job Position
keyword_terms = []

while True:
    keyword = input("Which Types Of Jobs You Are Looking For?: ")

    if keyword == '':
        break

    keyword_terms.append(keyword)

print(keyword_terms)

for keyword_item in keyword_terms:
    query += keyword_item

page = requests.get(BASE_URL + query)

contents = BeautifulSoup(page.content, "html.parser")

links = contents.findAll("a")

for link in contents.find_all("a", href = re.compile("(?<=/url\?q=)(htt.*://.*)")):
    splitted_link = re.split(":(?=http)", link["href"].replace("/url?q=", ''))

    try:
        req = requests.head(splitted_link[0])
        if req.status_code == 200:
            print(splitted_link[0])

    except requests.ConnectionError:
        print("Failed To Connect.")
        print("No Link Available!")



