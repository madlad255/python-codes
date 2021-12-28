import mysql.connector
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = ""

page = requests.get(url, headers={"User-Agent": "Catailyst Inc. catailyst333@gmail.com"})
soup = BeautifulSoup(page.text, 'lxml')

# check table tag
table = soup.find('table', {'summary':'Document Format Files'})
header = []

for i in table.find_all('th'):
    title = i.text
    header.append(title)

df = pd.DataFrame(columns = header)

lnks =[]
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data
print(df)