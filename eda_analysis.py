import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Excel File
file_name = "ApexPlanet_DataAnalytics_Dataset.xlsx"

try:
    df = pd.read_excel(file_name)
    print("Dataset Loaded Successfully")
except Exception as e:
    print("Error Loading Dataset:", e)
    exit()

# Display Information
print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nMissing Values")
print(df.isnull().sum())

# Convert Date Column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Fill Missing Age Values
df["Age"] = df["Age"].fillna(df["Age"].median())

# KPI Metrics

total_revenue = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
avg_order_value = df["Total_Sales"].mean()

print("\n========== KPI ==========")
print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Orders       : {total_orders}")
print(f"Total Customers    : {total_customers}")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")

# 1. Sales Distribution

plt.figure(figsize=(8,5))
sns.histplot(df["Total_Sales"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

# 2. Category Revenue

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()

# 3. City Revenue

city_sales = (
    df.groupby("City")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar")
plt.title("Revenue by City")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("city_revenue.png")
plt.show()

# 4. Gender Distribution

plt.figure(figsize=(6,6))
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.show()

# 5. Monthly Revenue Trend

df["Month"] = df["Order_Date"].dt.strftime("%Y-%m")

monthly_sales = (
    df.groupby("Month")["Total_Sales"]
    .sum()
)

plt.figure(figsize=(12,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# 6. Correlation Heatmap

corr_cols = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

plt.figure(figsize=(8,6))
sns.heatmap(
    df[corr_cols].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# 7. Age vs Sales

plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Age",
    y="Total_Sales",
    hue="Gender"
)
plt.title("Age vs Total Sales")
plt.tight_layout()
plt.savefig("age_vs_sales.png")
plt.show()

# 8. Top Products

top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY")