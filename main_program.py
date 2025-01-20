from utils.data_analysis import analyze_data
from utils.clustering import cluster_customers
from utils.recommendations import recommend_products

def main():
    file_path = "customer_purchases.csv"

    # Step 1: Data Analysis
    top_products, top_categories, avg_spending = analyze_data(file_path)
    print("Data Analysis Completed.")
    print("Top-selling Products:\n", top_products)
    print("Top Categories:\n", top_categories)

    # Step 2: Customer Classification
    customer_segments = cluster_customers(file_path)
    print("Customer Classification Completed.")
    print(customer_segments)

    # Step 3: Product Recommendation
    customer_id = "C0001"
    recommendations = recommend_products(file_path, customer_id)
    print(f"Recommended Products for {customer_id}:\n", recommendations)

if __name__ == "__main__":
    main()
