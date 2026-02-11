import requests
from bs4 import BeautifulSoup
from time import sleep

def scrape_page(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[Error] Could not fetch page {page_number}: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".product_pod")

    results = []
    for item in items:
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text
        rating = item.p["class"][1]
        link = "https://books.toscrape.com/catalogue/" + item.h3.a["href"]

        results.append({
            "title": title,
            "price": price,
            "rating": rating,
            "link": link
        })

    print(f"[✔] Scraped page {page_number}")
    sleep(1)  # جلوگیری از بلاک شدن

    return results
