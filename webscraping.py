import sys
print("stdout encoding:",sys.stdout.encoding)
import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
response=requests.get(url, timeout=10)
print(response.status_code,len(response.text))

soup = BeautifulSoup(response.text,"html.parser")

ilkalinti=soup.find("div", class_="quote")
alinti=ilkalinti.find("span", class_="text").text
yazar=ilkalinti.find("small", class_="author").text

print("Alıntı:",alinti)
print("Yazar:",yazar)

for i, q in enumerate(soup.select("div.quote"), start=1):
    metin = q.find("span", class_="text").get_text(strip=True)
    yazar = q.find("small", class_="author").get_text(strip=True)
    print(f"{i}) {yazar} — {metin}")



