# Import necessary libraries
import pandas as pd

# Load datasets
file_path1 = "Absence_3term201819_nat_reg_la_sch.csv"
file_path2 = "Absence_3term201819_national_characteristics.csv"

# Load the datasets
dataset1 = pd.read_csv(file_path1)
dataset2 = pd.read_csv(file_path2)

# Data Cleaning for Dataset 1
# Removing duplicate rows
dataset1_cleaned = dataset1.drop_duplicates()

# Handling missing values
dataset1_cleaned.fillna({
    col: dataset1_cleaned[col].mean() if dataset1_cleaned[col].dtype != 'object' else "Unknown"
    for col in dataset1_cleaned.columns
}, inplace=True)

# Data Cleaning for Dataset 2
dataset2_cleaned = dataset2.drop_duplicates()

# Handling missing values
dataset2_cleaned.fillna({
    col: dataset2_cleaned[col].mean() if dataset2_cleaned[col].dtype != 'object' else "Unknown"
    for col in dataset2_cleaned.columns
}, inplace=True)

# Save cleaned datasets
dataset1_cleaned.to_csv("Cleaned_Absence_3term201819_nat_reg_la_sch.csv", index=False)
dataset2_cleaned.to_csv("Cleaned_Absence_3term201819_national_characteristics.csv", index=False)

print("Data cleaned and saved successfully.")

# File paths
file_path_char = "ks2mats_ud_school_char.csv"
file_path_prog_rwm = "ks2mats_ud_school_prog_rwm.csv"
file_path_hierarchy = "mats_ud_hierarchy.csv"

# Load datasets
school_char = pd.read_csv(file_path_char, encoding='utf-8')
school_prog_rwm = pd.read_csv(file_path_prog_rwm, encoding='utf-8')
school_hierarchy = pd.read_csv(file_path_hierarchy, encoding='ISO-8859-1')

# Step 1: Data Cleaning for Each Dataset
# 1.1 School Characteristics Dataset
school_char_cleaned = school_char.drop_duplicates()  # Remove duplicates
school_char_cleaned.fillna("Unknown", inplace=True)  # Handle missing values
school_char_cleaned.rename(columns={"urn": "URN"}, inplace=True)  # Normalize column name

# 1.2 School Progress Dataset
school_prog_rwm_cleaned = school_prog_rwm.drop_duplicates()
school_prog_rwm_cleaned.fillna("Unknown", inplace=True)
school_prog_rwm_cleaned.rename(columns={"urn": "URN"}, inplace=True)

# 1.3 School Hierarchy Dataset
school_hierarchy_cleaned = school_hierarchy.drop_duplicates()
school_hierarchy_cleaned.fillna("Unknown", inplace=True)

# Step 2: Merge Datasets
merged_data = pd.merge(school_char_cleaned, school_prog_rwm_cleaned, on="URN", how="inner")
merged_data = pd.merge(merged_data, school_hierarchy_cleaned, on="URN", how="inner")

# Step 3: Clean 'value_x' Column
merged_data['value_x_cleaned'] = (
    merged_data['value_x']
    .astype(str)
    .str.replace('%', '', regex=False)
    .str.replace(r'[^\d.-]', '', regex=True)
)
merged_data['value_x_cleaned'] = pd.to_numeric(merged_data['value_x_cleaned'], errors='coerce')

# Step 4: Final Cleaning
merged_data.drop_duplicates(inplace=True)

# Step 5: Save Cleaned Data
merged_data.to_csv("cleaned_merged_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_merged_data.csv'.")
