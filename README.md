Advanced Web Scraper with SQLite and CSV Output

An advanced web scraper built with Python that extracts data from multiple pages, stores the data in an SQLite database, and saves the output to a CSV file.

✨ Features

· ✅ Supports data extraction from multiple pages (pagination)
· ✅ Extracts title, price, rating, and link (configurable)
· ✅ Saves data to SQLite database
· ✅ Saves data to CSV file
· ✅ Handles errors, timeouts, and retries
· ✅ Clean and structured code with professional folder organization

📁 Project Structure

```
advanced_scraper/
│
├── scraper.py          # Contains web scraping logic
├── database.py         # Handles SQLite database connection and queries
├── save_to_csv.py      # Saves scraped data to CSV file
├── main.py             # Main script that runs the scraper
└── requirements.txt    # Required Python libraries
```

🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/advanced_scraper.git
cd advanced_scraper
```

2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

💻 Usage

Run the scraper

```bash
python main.py
```

The scraper will fetch data from books.toscrape.com, extract product title, price, rating, and link, and save the data in two formats:

· SQLite database: products.db
· CSV file: products.csv

⚙️ Customization

Scrape specific pages

Modify the run_scraper() function in main.py:

```python
run_scraper(start_page=1, end_page=5)  # Change page range as needed
```

Change extracted data

Modify the scrape_page() function in scraper.py.

🛡️ Error Handling

· Timeout: Retries if server response takes too long
· Retry: Up to 3 retries before skipping a page
· Invalid data: Skips items that cannot be extracted

📊 Output

After running the scraper, the following files are generated:

· SQLite Database (products.db) — Contains all scraped product data
· CSV File (products.csv) — Contains all scraped product data in CSV format

Example CSV Output

```csv
title,price,rating,link
"A Light in the Attic","$51.77","Three","https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
"Sharp Objects","$47.75","Five","https://books.toscrape.com/catalogue/sharp-objects_999/index.html"
...
```

🤝 Contributing

Feel free to fork the repository, create issues, and submit pull requests. Contributions are welcome!

📄 License

This project is licensed under the MIT License — see the LICENSE file for details.

📞 Support
For bug reports or feature suggestions:
·Create an Issue on GitHub   
·Username: MhdVesre00

⭐ If you found this project useful, please give it a star on GitHub!
