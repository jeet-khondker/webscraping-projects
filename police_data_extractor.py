import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.policeone.com/law-enforcement-directory/"

main_page = requests.get(BASE_URL)
soup = BeautifulSoup(main_page.content, "html.parser")

container = soup.findAll("div", attrs = {"class" : "Table-body"})
for row in container:
    for item in row.findAll('a'):

        # Extracting Link For Navigation
        text = item.get("href").split('/')
        
        # Generating New URL
        NEW_LOOKUP_URL = BASE_URL + text[2] + '/' + text[3]

        navigate_page = requests.get(NEW_LOOKUP_URL)
        navigate_soup = BeautifulSoup(navigate_page.content, "html.parser")

        article_container = navigate_soup.findAll("article", attrs = {"class" : "Article"})

        for data in article_container:
            for title in data.findAll("h1", attrs = {"class" : "Article-p Article-p--heading"}):
                txt_file = open("police_data.txt", "a+")
                txt_file.write("Agency: \n" + title.text)

                for info in data.findAll("dl", attrs = {"class" : "DefList"}):
                    txt_file.write(info.text + "\n")

                    with open("police_data.txt", 'r') as readFile:
                        filedata = readFile.read()

                    filedata = filedata.replace("Country", "Station Name")
                    filedata = filedata.replace("Address 1", "Address")
                    
                    with open("police_data.txt", 'w') as writeFile:
                        writeFile.write(filedata)