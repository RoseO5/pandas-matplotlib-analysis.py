cat > analyze_sales.py <<'EOF'
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Preview data
print("Preview of dataset:")
print(df.head())

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Analysis: Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Analysis: Total sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Visualization 1: Sales by Region (Bar Chart)
plt.figure(figsize=(6,4))
sales_by_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.close()

# Visualization 2: Sales by Product (Bar Chart)
plt.figure(figsize=(6,4))
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.close()

print("\\nCharts saved: sales_by_region.png, sales_by_product.png")
EOF
