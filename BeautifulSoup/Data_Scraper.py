import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}
r = requests.get("https://www.amazon.in/s?k=pixel&crid=2KPBQCLUJ4MH1&sprefix=pixe%2Caps%2C287&ref=nb_sb_noss_2", headers = headers)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
spans = soup.select('span.a-size-medium.a-color-base.a-text-normal')
data = {'title':[], 'price':[]}
i = 1
prices = soup.select('span.a-price-whole')
for price in prices:
    data['price'].append(price.string)
    # print(price.string)
for span in spans:
    if len(data['price'])==len(data['title']):
        break
    data['title'].append(span.string)
    # print(span.string)
    i+=1
df = pd.DataFrame(data)
df.to_excel('./Data.xlsx', index=False)