import requests
from bs4 import BeautifulSoup   

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.title.text)

titles = [a.get("title") for a in soup.select("article.product_pod h3 a")]
print(len(titles))
print(titles[:5])

prices = [p.get_text(strip=True)for p in soup.select("p.price_color")]
print(len(prices), "fiyat bulundu")
print(prices[:5])

print(len(titles),len(prices))

for i, pod in enumerate(soup.select("article.product_pod"), start=1):
    title = pod.h3.a.get("title")

    price_tag = pod.select_one("p.price_color")
    price = price_tag.get_text(strip=True)

    print(f"{i}. {title} - {price}")
    import re
    num = float(re.sub(r"[^\d.]", "", price))

    most_expensive = max(titles_numeric_prices, key=lambda x: x[1])
    print("En pahalı:", most_expensive[0], most_expensive[1])


