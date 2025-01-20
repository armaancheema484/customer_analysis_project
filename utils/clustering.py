import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_customers(file_path, n_clusters=3):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Aggregate customer data: Frequency, Total Spending
    customer_data = df.groupby('Customer ID').agg({
        'Purchase Amount': 'sum', 
        'Product ID': 'count'
    }).rename(columns={'Purchase Amount': 'Total Spending', 'Product ID': 'Frequency'})

    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(customer_data)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    customer_data['Cluster'] = kmeans.fit_predict(scaled_data)

    # Add cluster labels
    cluster_labels = {0: "High Spenders", 1: "Medium Spenders", 2: "Occasional Buyers"}
    customer_data['Segment'] = customer_data['Cluster'].map(cluster_labels)

    return customer_data

if __name__ == "__main__":
    clustered_data = cluster_customers("customer_purchases.csv")
    print(clustered_data)
