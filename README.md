# 🛒 Blinkit Grocery Sales Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![SQL](https://img.shields.io/badge/SQL-Analysis-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)

## 📌 Project Overview

This project performs an end-to-end analysis of **Blinkit grocery sales data** using **Python, Pandas, SQLite, SQL, and Power BI**.

The objective is to understand sales performance across product categories, outlet types, outlet sizes, location tiers, fat-content preferences, pricing segments, and customer ratings.

The project follows a real-world data analyst workflow:

```text
Raw CSV Dataset
      ↓
Python + Pandas
      ↓
Data Cleaning & Transformation
      ↓
SQLite Database
      ↓
SQL Analysis & KPI Calculation
      ↓
Excel Output
      ↓
Power BI Dashboard
      ↓
Business Insights
```

---

## 🎯 Business Objective

The analysis aims to answer important retail business questions such as:

* What is the total sales revenue?
* What is the average sales per item?
* What is the average customer rating?
* Which product categories generate the highest sales?
* Do Low Fat or Regular products perform better?
* Which outlet size generates the most revenue?
* Which location tier performs best?
* Which outlet type is most profitable?
* Which price range generates the highest sales?
* Which product categories rank highest in sales?

---

## 🛠️ Technologies Used

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| **Python**       | Data processing and automation           |
| **Pandas**       | Data cleaning and transformation         |
| **SQLite**       | Local relational database                |
| **SQL**          | KPI calculation and business analysis    |
| **Excel**        | Analysis output and Power BI data source |
| **Power BI**     | Interactive dashboard                    |
| **Git & GitHub** | Version control and portfolio            |

---

## 📂 Dataset

The project uses the **BlinkIT Grocery Dataset** containing grocery sales and outlet information.

### Important columns

```text
Item_Fat_Content
Item_Type
Item_MRP
Outlet_Size
Outlet_Location_Type
Outlet_Type
Item_Visibility
Item_Rating
Sales
```

### Dataset Source

[Kaggle — BlinkIT Grocery Dataset](https://www.kaggle.com/datasets/mukeshgadri/blinkit-dataset)

> Download `BlinkIT Grocery Data.csv` and place it in the project root directory before running the Python script.

---

## 📁 Project Structure

```text
Blinkit-Grocery-Sales-Analysis/
│
├── BlinkIT Grocery Data.csv
├── blinkit_analysis.py
├── blinkit.db
├── blinkit_analysis.xlsx
├── dashboard.png
└── README.md
```

### File Description

| File                       | Description                                |
| -------------------------- | ------------------------------------------ |
| `BlinkIT Grocery Data.csv` | Original dataset                           |
| `blinkit_analysis.py`      | Complete Python + SQLite analysis pipeline |
| `blinkit.db`               | SQLite database containing cleaned data    |
| `blinkit_analysis.xlsx`    | SQL analysis results exported to Excel     |
| `dashboard.png`            | Power BI dashboard screenshot              |
| `README.md`                | Project documentation                      |

---

# 🔄 Project Workflow

## 1. Data Collection

The Blinkit grocery dataset is downloaded from Kaggle in CSV format.

```text
BlinkIT Grocery Data.csv
```

---

## 2. Data Loading

Python and Pandas are used to load the CSV dataset.

```python
import pandas as pd

df = pd.read_csv("BlinkIT Grocery Data.csv")
```

The dataset is inspected for:

* Number of rows
* Number of columns
* Column names
* Missing values
* Duplicate records
* Data types

---

## 3. Data Cleaning

The Python script performs several preprocessing steps.

### Standardizing Fat Content

The dataset contains inconsistent labels such as:

```text
LF
low fat
Low Fat
reg
Regular
```

These are standardized to:

```text
Low Fat
Regular
```

Example:

```python
df["Item_Fat_Content"] = df["Item_Fat_Content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "reg": "Regular"
})
```

### Missing Values

Missing numerical values are handled using the median.

Categorical missing values are replaced with:

```text
Unknown
```

### Duplicate Records

Duplicate rows are removed using Pandas.

---

# 🗄️ SQLite Database

After cleaning, the data is loaded into a SQLite database.

```text
blinkit.db
```

The main table is:

```text
blinkit
```

The Python script automatically creates the table using:

```python
df.to_sql(
    "blinkit",
    conn,
    if_exists="replace",
    index=False
)
```

This allows SQL queries to be performed directly on the cleaned dataset.

---

# 📊 KPI Analysis

The project calculates four core business KPIs.

## 1. Total Sales

```sql
SELECT
    ROUND(SUM(Sales), 2) AS total_sales
FROM blinkit;
```

## 2. Average Sales

```sql
SELECT
    ROUND(AVG(Sales), 2) AS avg_sales
FROM blinkit;
```

## 3. Average Customer Rating

```sql
SELECT
    ROUND(AVG(Item_Rating), 2) AS avg_rating
FROM blinkit;
```

## 4. Total Items

```sql
SELECT
    COUNT(*) AS total_items
FROM blinkit;
```

---

# 📈 SQL Analysis

## Sales by Item Type

Identifies the highest-revenue product categories.

```sql
SELECT
    Item_Type,
    ROUND(SUM(Sales), 2) AS total_sales,
    COUNT(*) AS item_count
FROM blinkit
GROUP BY Item_Type
ORDER BY total_sales DESC;
```

---

## Sales by Fat Content

Compares customer demand for Low Fat and Regular products.

```sql
SELECT
    Item_Fat_Content,
    ROUND(SUM(Sales), 2) AS total_sales,
    COUNT(*) AS item_count,
    ROUND(AVG(Item_Rating), 2) AS avg_rating
FROM blinkit
GROUP BY Item_Fat_Content;
```

---

## Sales by Outlet Size

Analyzes performance across:

```text
Small
Medium
Large
```

```sql
SELECT
    Outlet_Size,
    ROUND(SUM(Sales), 2) AS total_sales,
    COUNT(*) AS item_count,
    ROUND(AVG(Sales), 2) AS avg_sales_per_item
FROM blinkit
GROUP BY Outlet_Size
ORDER BY total_sales DESC;
```

---

## Sales by Location Tier

Compares outlet performance across different location tiers.

```sql
SELECT
    Outlet_Location_Type,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(AVG(Item_Rating), 2) AS avg_rating
FROM blinkit
GROUP BY Outlet_Location_Type
ORDER BY total_sales DESC;
```

---

## Sales by Outlet Type

```sql
SELECT
    Outlet_Type,
    ROUND(SUM(Sales), 2) AS total_sales,
    COUNT(*) AS item_count,
    ROUND(AVG(Sales), 2) AS avg_sales
FROM blinkit
GROUP BY Outlet_Type
ORDER BY total_sales DESC;
```

---

# 💰 Price Range Analysis

Products are divided into four price segments:

```text
Budget     → Under 50
Mid        → 50–100
Premium    → 100–200
Luxury     → 200+
```

SQL analysis:

```sql
SELECT
    Price_Range,
    COUNT(*) AS item_count,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(AVG(Item_Rating), 2) AS avg_rating
FROM blinkit
GROUP BY Price_Range
ORDER BY total_sales DESC;
```

This helps identify the price segment contributing the most revenue.

---

# 🏆 Window Function Analysis

A `RANK()` window function is used to rank product categories based on total sales.

```sql
SELECT
    Item_Type,
    ROUND(SUM(Sales), 2) AS total_sales,

    RANK() OVER (
        ORDER BY SUM(Sales) DESC
    ) AS sales_rank

FROM blinkit

GROUP BY Item_Type

ORDER BY sales_rank;
```

This demonstrates intermediate SQL skills beyond basic aggregation.

---

# 📊 Power BI Dashboard

The cleaned data and SQL analysis results are exported to:

```text
blinkit_analysis.xlsx
```

This Excel file is then imported into Power BI to build an interactive dashboard.

## Dashboard KPIs

The dashboard contains:

* Total Sales
* Average Sales
* Average Customer Rating
* Total Items

## Dashboard Visualizations

### Product Analysis

* Sales by Item Type
* Sales by Fat Content
* Sales by Price Range

### Outlet Analysis

* Sales by Outlet Type
* Sales by Outlet Size
* Sales by Location Tier

### Interactive Filters

Slicers are included for:

```text
Item Type
Item Fat Content
Outlet Size
Outlet Location Type
Outlet Type
Price Range
```

---

# 📸 Dashboard Preview

Add your Power BI screenshot here after creating the dashboard:

```markdown
![Blinkit Power BI Dashboard](dashboard.png)
```

---

# 🔍 Key Business Insights

The analysis focuses on identifying:

* Total revenue generated across all outlets
* Highest-performing product categories
* Sales comparison between Low Fat and Regular products
* Best-performing outlet size
* Best-performing location tier
* Highest-performing outlet type
* Most profitable price segment
* Relationship between customer ratings and sales
* Top-ranked product categories
* Outlet type and location combinations with the strongest sales

> Actual numerical insights should be added here after running the analysis and Power BI dashboard.

---

# ▶️ How to Run the Project

## Step 1 — Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd Blinkit-Grocery-Sales-Analysis
```

---

## Step 2 — Install Dependencies

```bash
pip install pandas openpyxl
```

---

## Step 3 — Add the Dataset

Download:

```text
BlinkIT Grocery Data.csv
```

from Kaggle and place it in the project folder.

---

## Step 4 — Run the Python Script

```bash
python blinkit_analysis.py
```

The script will:

```text
Load CSV
   ↓
Clean data
   ↓
Create SQLite database
   ↓
Run SQL queries
   ↓
Calculate KPIs
   ↓
Perform ranking analysis
   ↓
Export Excel results
```

---

## Step 5 — Open SQLite Database

The script creates:

```text
blinkit.db
```

You can open the database using a SQLite extension in VS Code.

Example:

```sql
SELECT *
FROM blinkit
LIMIT 10;
```

---

## Step 6 — Open Power BI

Open Power BI Desktop.

Select:

```text
Get Data
    ↓
Excel
    ↓
blinkit_analysis.xlsx
```

Load the required sheets and build the dashboard.

---

# 🧠 Skills Demonstrated

### Python

* Pandas
* Data cleaning
* Missing-value handling
* Duplicate removal
* Data transformation
* Excel export
* SQLite integration

### SQL

* `SELECT`
* `SUM`
* `AVG`
* `COUNT`
* `GROUP BY`
* `ORDER BY`
* `HAVING`
* `CASE`
* `RANK()`
* Window Functions
* Aggregations

### Power BI

* KPI Cards
* Bar Charts
* Column Charts
* Donut Charts
* Slicers
* Dashboard Design
* Business Storytelling

---

# 💼 Interview Value

This project demonstrates an end-to-end data analyst workflow:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Database Management
      ↓
SQL Analysis
      ↓
KPI Development
      ↓
Business Insights
      ↓
Data Visualization
```

It demonstrates both **technical SQL skills** and **business-oriented analytical thinking**.

---

# 📝 Resume Project Description

**Blinkit Grocery Sales Analysis | Python, SQL, SQLite, Power BI**

> Built an end-to-end retail sales analysis pipeline using Python and Pandas for data cleaning, SQLite for database management and SQL-based KPI analysis, and Power BI for interactive visualization. Analyzed product categories, outlet types, location tiers, pricing segments, fat-content preferences, and customer ratings to identify key sales trends and business insights.

---

# 🚀 Future Improvements

Possible extensions include:

* Add monthly/seasonal sales analysis
* Analyze sales and item visibility correlation
* Build predictive sales models
* Add customer segmentation
* Create automated Power BI refresh
* Add advanced DAX measures
* Deploy the dashboard online
* Add forecasting using Machine Learning

---

# 👨‍💻 Author

**Akash**

Data Analytics Portfolio Project

### Skills

```text
Python
SQL
SQLite
Pandas
Power BI
Data Analysis
Data Visualization
Git & GitHub
```

---

## ⭐ Project Highlights

```text
✔ Python + Pandas Data Cleaning
✔ SQLite Database
✔ SQL KPI Analysis
✔ GROUP BY & HAVING
✔ CASE Statements
✔ Window Functions
✔ Sales Analysis
✔ Outlet Performance Analysis
✔ Power BI Dashboard
✔ Business Insights
✔ End-to-End Data Analytics Workflow
```

---

## 📚 Dataset Reference

Kaggle BlinkIT Grocery Dataset:

https://www.kaggle.com/datasets/mukeshgadri/blinkit-dataset

---

⭐ **If you found this project useful, consider giving the repository a star!**
