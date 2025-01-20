import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def recommend_products(file_path, customer_id):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Create a customer-product matrix
    customer_product_matrix = pd.crosstab(df['Customer ID'], df['Product ID'])

    # Compute similarity
    similarity = cosine_similarity(customer_product_matrix)

    # Get the index of the customer
    customer_idx = list(customer_product_matrix.index).index(customer_id)

    # Get similar customers
    similar_customers = similarity[customer_idx].argsort()[-6:-1][::-1]  # Top 5

    # Recommend products based on similar customers
    recommended_products = set()
    for idx in similar_customers:
        customer_products = customer_product_matrix.iloc[idx].loc[
            customer_product_matrix.iloc[idx] > 0
        ].index
        recommended_products.update(customer_products)

    return list(recommended_products)

if __name__ == "__main__":
    recommendations = recommend_products("customer_purchases.csv", "C0001")
    print("Recommended Products:\n", recommendations)
