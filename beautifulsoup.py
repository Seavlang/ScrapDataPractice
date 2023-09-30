# import module
import requests
import json
from bs4 import BeautifulSoup


# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata("https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/")
soup = BeautifulSoup(htmldata, 'html.parser')
pickup_lines = {}
titles = soup.find_all("h2", class_="body-h2")
for title in titles:
    heading = title.text
    pickup_lines[heading] = []
    # innerContent = soup.find('ul', class_="css-19p7hma")
    innerContent = title.findNext('ul', class_="css-19p7hma")
    li_items = innerContent.find_all('li')
    for li in li_items:
        pickup_lines[title.text].append(li.text.strip())
with open("pickupline.json", "w") as writeJSON:
    json.dump(pickup_lines,writeJSON,ensure_ascii=False,indent=4)