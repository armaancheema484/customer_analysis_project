import pandas as pd

def analyze_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Top-selling products and categories
    top_products = df['Product ID'].value_counts().head(10)
    top_categories = df['Product Category'].value_counts().head(5)

    # Average spending per customer
    avg_spending = df.groupby('Customer ID')['Purchase Amount'].mean()

    return top_products, top_categories, avg_spending

if __name__ == "__main__":
    top_products, top_categories, avg_spending = analyze_data("customer_purchases.csv")
    print("Top-selling Products:\n", top_products)
    print("Top Categories:\n", top_categories)
    print("Average Spending per Customer:\n", avg_spending)
