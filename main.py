from scraper import scrape_page
from database import create_table, insert_data
from save_to_csv import save_to_csv

all_data = []

def run_scraper(start_page=1, end_page=5):
    create_table()

    for page in range(start_page, end_page + 1):
        data = scrape_page(page)

        if not data:
            continue

        for item in data:
            insert_data(
                item["title"],
                item["price"],
                item["rating"],
                item["link"]
            )
            all_data.append(item)

    if all_data:
        save_to_csv(all_data)

    print("\n[✔] Done! Data saved in database and CSV.")

if __name__ == "__main__":
    run_scraper()
