import pandas as pd
import random
from datetime import datetime, timedelta

def generate_dataset(file_path="customer_purchases.csv"):
    """Generates a synthetic dataset of customer purchase history."""
    num_customers = 500
    num_products = 50
    num_records = 5000
    products_per_day = 15  # Assign 15 products per day

    # Generate customers and products
    customers = [f"C{str(i).zfill(4)}" for i in range(1, num_customers + 1)]
    products = [f"P{str(i).zfill(4)}" for i in range(1, num_products + 1)]
    categories = ["Electronics", "Fashion", "Home", "Toys", "Books", "Sports"]

    # Generate a fixed list of dates in the last 2 years
    today = datetime.today()
    start_date = today - timedelta(days=730)  # Two years ago
    date_list = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(730)]

    # Initialize purchase records
    data = []
    date_index = 0

    for i in range(num_records):
        customer_id = random.choice(customers)
        product_id = products[i % len(products)]
        product_category = random.choice(categories)
        purchase_amount = round(random.uniform(10, 1000), 2)

        # Assign a date from the list, ensuring rotation every 15 products
        if i % products_per_day == 0 and i > 0:
            date_index += 1
        purchase_date = date_list[date_index % len(date_list)]

        # Add the record to the data list
        data.append([customer_id, product_id, product_category, purchase_amount, purchase_date])

    # Save the dataset to a CSV file
    df = pd.DataFrame(data, columns=["Customer ID", "Product ID", "Product Category", "Purchase Amount", "Purchase Date"])
    df.to_csv(file_path, index=False, date_format="%Y-%m-%d")
    print(f"Dataset generated successfully and saved to {file_path}")

if __name__ == "__main__":
    generate_dataset()
