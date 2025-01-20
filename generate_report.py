import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Helper function to save visuals
def plot_top_products(data, save_path):
    data.plot(kind="bar", figsize=(8, 5), color="skyblue", legend=False)
    plt.title("Top-Selling Products")
    plt.ylabel("Number of Purchases")
    plt.xlabel("Product ID")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_top_categories(data, save_path):
    data.plot(kind="bar", figsize=(8, 5), color="orange", legend=False)
    plt.title("Top Categories")
    plt.ylabel("Number of Purchases")
    plt.xlabel("Category")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Generate PDF report
def generate_pdf_report(output_file, top_products, top_categories, customer_segments, recommendations):
    # Create a PDF canvas
    pdf = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 50, "Retail Customer Analysis Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 80, f"Generated Report on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Section 1: Data Analysis
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 120, "1. Data Analysis")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 140, "Top-Selling Products:")
    pdf.drawImage("top_products.png", 50, height - 380, width=500, height=200)

    pdf.drawString(50, height - 410, "Top Categories:")
    pdf.drawImage("top_categories.png", 50, height - 610, width=500, height=200)

    # Add a new page for clusters and recommendations
    pdf.showPage()

    # Section 2: Customer Clusters
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "2. Customer Segmentation")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 80, "Customer Segments and their Key Characteristics:")

    y_position = height - 120
    for cluster, count in customer_segments['Segment'].value_counts().items():
        pdf.drawString(50, y_position, f"{cluster}: {count} customers")
        y_position -= 20

    # Section 3: Recommendations
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y_position - 40, "3. Product Recommendations")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y_position - 60, f"Recommendations for Customer 'C0001':")

    y_position -= 100
    for product in recommendations:
        pdf.drawString(50, y_position, f"  - Product ID: {product}")
        y_position -= 20

    # Save the PDF
    pdf.save()
    print(f"PDF report saved to {output_file}")

# Main function to generate report
def generate_report():
    # Load the dataset
    file_path = "customer_purchases.csv"
    df = pd.read_csv(file_path)

    # Top-selling products and categories
    top_products = df["Product ID"].value_counts().head(10)
    top_categories = df["Product Category"].value_counts().head(5)

    # Customer segmentation
    from utils.clustering import cluster_customers
    customer_segments = cluster_customers(file_path)

    # Product recommendations
    from utils.recommendations import recommend_products
    recommendations = recommend_products(file_path, "C0001")

    # Generate visuals
    plot_top_products(top_products, "top_products.png")
    plot_top_categories(top_categories, "top_categories.png")

    # Generate the PDF report
    generate_pdf_report(
        output_file="reports/analysis_report.pdf",
        top_products=top_products,
        top_categories=top_categories,
        customer_segments=customer_segments,
        recommendations=recommendations,
    )

if __name__ == "__main__":
    generate_report()
