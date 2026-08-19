import pandas as pd

# ==============================
# 1. Load Dataset
# ==============================

file_path = "data/BlinkIT Grocery Data.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==============================
# 2. Standardize Column Names
# ==============================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumn names:")
print(df.columns.tolist())


# ==============================
# 3. Preview Dataset
# ==============================

print("\nFirst 5 rows:")
print(df.head())


# ==============================
# 4. Dataset Information
# ==============================

print("\nDataset information:")
print(df.info())


# ==============================
# 5. Missing Values
# ==============================

print("\nMissing values:")
print(df.isnull().sum())


# ==============================
# 6. Duplicate Rows
# ==============================

print("\nDuplicate rows:")
print(df.duplicated().sum())


# ==============================
# 7. Statistics
# ==============================

print("\nStatistics:")
print(df.describe())


# ==============================
# 8. Fat Content Analysis
# ==============================

print("\nFat Content:")
print(df["item_fat_content"].value_counts())


# ==============================
# 9. Clean Fat Content
# ==============================

df["item_fat_content"] = df["item_fat_content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "reg": "Regular"
})

print("\nCleaned Fat Content:")
print(df["item_fat_content"].value_counts())


# ==============================
# 10. Item Type Analysis
# ==============================

print("\nItem Types:")
print(df["item_type"].value_counts())


# ==============================
# 11. Outlet Type Analysis
# ==============================

print("\nOutlet Types:")
print(df["outlet_type"].value_counts())


# ==============================
# 12. Outlet Size Analysis
# ==============================

print("\nOutlet Sizes:")
print(df["outlet_size"].value_counts())


# ==============================
# 13. Outlet Location Analysis
# ==============================

print("\nOutlet Location Types:")
print(df["outlet_location_type"].value_counts())


# ==============================
# 14. Missing Item Weight
# ==============================

print("\nMissing Item Weight:")
print(df["item_weight"].isnull().sum())


# ==============================
# 15. Save Cleaned Dataset
# ==============================

output_file = "data/blinkit_cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)