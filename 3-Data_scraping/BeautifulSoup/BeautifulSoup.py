from datetime import datetime
from bs4 import BeautifulSoup
import requests


url = 'https://ca.finance.yahoo.com/quote/%5EDJI?p=^DJI'
page = requests.get(url)
content = page.content

soup = BeautifulSoup(content, 'html.parser')

table = soup.find("div", {"id": "quote-summary"})

table_body = table.findAll('tbody')

for body in table_body:
    rows = body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        print(">>>>>", cols, '\n')

