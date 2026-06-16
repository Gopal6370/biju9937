# Exploratory Data Analysis (EDA) & Business Intelligence Report

## Project Title

Customer Sales Analysis and Business Intelligence using Python & SQL

## Objective

The primary objective of this project is to perform Exploratory Data Analysis (EDA) on customer sales data and derive meaningful business insights through data visualization and SQL analysis. The project aims to identify trends, patterns, and key performance indicators that support data-driven decision-making.

---

## Dataset Description

The dataset contains sales transaction records with customer demographics, product information, order details, and revenue data.

### Dataset Features

| Column Name   | Description                |
| ------------- | -------------------------- |
| Order_ID      | Unique order identifier    |
| Order_Date    | Date of purchase           |
| Customer_ID   | Unique customer identifier |
| Customer_Name | Customer name              |
| Age           | Customer age               |
| Gender        | Customer gender            |
| City          | Customer city              |
| Product       | Product purchased          |
| Category      | Product category           |
| Quantity      | Quantity purchased         |
| Unit_Price    | Price per unit             |
| Total_Sales   | Total revenue generated    |

---

## Tools and Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* SQLite
* Visual Studio Code
* Excel

---

## Data Cleaning Process

The following preprocessing steps were performed:

1. Loaded dataset from Excel file.
2. Checked for missing values.
3. Converted date columns to datetime format.
4. Verified data types of all columns.
5. Prepared data for visualization and SQL analysis.

---

## Exploratory Data Analysis

### 1. Sales Distribution Analysis

A histogram was created to analyze the distribution of total sales values across all transactions.

**Observation:**

* Sales values are distributed across multiple ranges.
* High-value transactions contribute significantly to total revenue.

### 2. Revenue by Product Category

A category-wise revenue analysis was performed.

**Observation:**

* Certain product categories contribute more revenue than others.
* High-performing categories can be prioritized for future business strategies.

### 3. Revenue by City

City-wise sales analysis was conducted to identify top-performing regions.

**Observation:**

* Major cities generated the highest sales revenue.
* Regional performance differences were observed.

### 4. Gender Distribution

Customer distribution based on gender was visualized.

**Observation:**

* Customer participation varies between gender groups.
* Provides demographic insights for targeted marketing.

### 5. Monthly Revenue Trend

Monthly revenue trends were analyzed using time-series visualization.

**Observation:**

* Revenue fluctuations indicate seasonal purchasing patterns.
* Monthly analysis helps forecast future sales.

### 6. Correlation Analysis

A correlation heatmap was generated for numerical features.

**Observation:**

* Quantity and Total Sales show a positive relationship.
* Unit Price significantly influences overall revenue.

### 7. Product Performance Analysis

Top-performing products were identified based on total revenue generated.

**Observation:**

* A small group of products contributes a large share of revenue.
* These products can be considered business drivers.

---

## SQL Business Analysis

Business-oriented SQL queries were executed to answer key questions.

### Business Questions

1. What is the total revenue generated?
2. How many orders were placed?
3. How many unique customers exist?
4. Which products generate the highest revenue?
5. Which categories perform best?
6. Which cities contribute the most revenue?
7. Who are the top customers by revenue?
8. What is the monthly revenue trend?
9. Which products have the highest sales quantity?
10. How does revenue vary across genders?

---

## Key Business Insights

* Top-performing products contribute significantly to overall revenue.
* Revenue is concentrated in a few high-performing categories.
* Certain cities generate a larger share of total sales.
* Monthly trends reveal seasonal sales fluctuations.
* Customer demographics influence purchasing behavior.
* Quantity sold directly impacts revenue generation.

---

## Dashboard Design

A Business Intelligence Dashboard was designed to visualize important KPIs and trends.

### Dashboard Components

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Revenue by Category
* Revenue by City
* Monthly Revenue Trend
* Gender Distribution
* Top Products by Revenue

---

## Conclusion

This project successfully demonstrated the application of Exploratory Data Analysis and Business Intelligence techniques using Python and SQL. Through data cleaning, visualization, statistical analysis, and SQL querying, valuable business insights were extracted from raw sales data.

The project highlights the importance of data analytics in understanding customer behavior, evaluating product performance, and supporting strategic business decisions.

---

## Future Enhancements

* Interactive Power BI Dashboard
* Sales Forecasting using Machine Learning
* Customer Segmentation Analysis
* Predictive Analytics Models
* Real-Time Business Intelligence Reporting

---

### Author

**Balgopal Khanda**

Data Analytics Internship Project

ApexPlanet Software Pvt. Ltd.
