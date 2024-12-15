# Visualization: Progress Scores by Socio-Economic Status
plt.figure(figsize=(8, 6))
sns.barplot(x='TrustName', y='value_x_cleaned', data=cleaned_data, ci=None)
plt.title("Progress Scores by Trust")
plt.xlabel("Trust Name")
plt.ylabel("Progress Score")
plt.xticks(rotation=45)
plt.show()


# Create a subset for FSM and Non-FSM
boxplot_data = cleaned_data[cleaned_data['measure'].isin(['matprog_fsm6cla1a', 'matprog_notfsm6cla1a'])]
boxplot_data['Student Group'] = boxplot_data['measure'].replace({
    'matprog_fsm6cla1a': 'FSM Students',
    'matprog_notfsm6cla1a': 'Non-FSM Students'
})

# Boxplot: Comparison of Progress Scores
plt.figure(figsize=(8, 6))
sns.boxplot(x='Student Group', y='value', data=boxplot_data, palette="Set2")
plt.title("Comparison of Maths Progress for FSM and Non-FSM Students")
plt.xlabel("Student Group")
plt.ylabel("Progress Score")
plt.show()



# Attendance vs Progress Scores Visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(x='AttendanceRate', y='value_x_cleaned', data=cleaned_data)
plt.axvline(x=85, color='red', linestyle='--', label='Threshold (85%)')
plt.title("Attendance Rate vs Progress Score")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("Progress Score")
plt.legend()
plt.show()




# Feature Importance Visualization
import pandas as pd

feature_importances = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_regressor.feature_importances_
})
feature_importances.sort_values(by="Importance", ascending=False, inplace=True)

print("Feature Importances:")
print(feature_importances)
