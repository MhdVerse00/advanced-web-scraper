import csv

def save_to_csv(data, filename="products.csv"):
    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"[✔] Data saved to {filename}")
