import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
cleaned_data = pd.read_csv("cleaned_merged_data.csv")

# Summary Statistics
print(cleaned_data.describe())

# Visualization: Distribution of Progress Scores
plt.figure(figsize=(8, 6))
sns.histplot(cleaned_data['value_x_cleaned'], kde=True, bins=30, color='blue')
plt.title("Distribution of Progress Scores")
plt.xlabel("Progress Score")
plt.ylabel("Frequency")
plt.show()
