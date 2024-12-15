# CW2_BEMM457_AbhishekPandey_740031609
# **Analyzing Factors Influencing Student Performance**

## **Overview**
This project investigates the key factors influencing student performance in primary and secondary education using advanced data analytics techniques. The study focuses on demographic characteristics, attendance patterns, and resource availability, providing actionable insights to policymakers and educators for improving equity and outcomes in education.

The analysis leverages descriptive and predictive analytics, utilizing datasets from the UK Department for Education and UNESCO. Key techniques include data cleaning, visualizations, regression modeling, and Random Forest predictions.

---

## **Datasets**
The analysis relies on the following datasets:
1. **UK Department for Education Data**: Provides detailed school-level data on student demographics, attendance rates, and academic performance for primary and secondary schools from 2015–2022.
2. **UNESCO Educational Data**: Offers a global perspective with indicators like parental education and resource availability.

### **Key Variables**
- **Demographic Information**: Socioeconomic status, parental education.
- **Attendance Patterns**: Percentage of days attended.
- **Academic Performance**: Progress scores in mathematics (FSM and non-FSM students).
- **Institutional Resources**: Trust performance scores and resource indicators.

---

## **Project Workflow**
### **1. Data Cleaning and Preprocessing**
- Removing duplicates and handling missing values.
- Normalizing column names for consistency across datasets.
- Merging datasets on the common identifier (`URN`).
- Cleaning and transforming columns like `value_x` for numerical analysis.

### **2. Descriptive Analytics**
- Statistical summaries of variables such as progress scores and attendance rates.
- Visualizations including histograms, bar charts, and scatterplots to reveal trends and disparities.

### **3. Predictive Analytics**
- **Linear Regression**: Quantifies the relationship between predictors (e.g., attendance, socioeconomic background) and progress scores.
- **Random Forest Regressor**: Captures nonlinear relationships and identifies the most important factors affecting performance.
- Residual and feature importance analysis to validate model accuracy.

### **4. Attendance Analysis**
- A focused analysis of attendance thresholds (e.g., 85%) and their impact on academic outcomes.
- Boxplots comparing FSM and non-FSM student performance.

---

## **How to Run the Code**
### **Requirements**
Install the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Use the command below to install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
