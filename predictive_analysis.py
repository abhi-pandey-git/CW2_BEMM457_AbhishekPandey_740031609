# Linear Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Prepare Data for Regression
X = cleaned_data[['value_x_cleaned']].dropna()  # Ensure no missing values
y = cleaned_data['avg_trust_score'].dropna()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Prediction and Evaluation
y_pred = regressor.predict(X_test)
print("Linear Regression R-squared:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Random Forest Regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

# Train Random Forest Regressor
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)

# Cross-Validation
rf_scores = cross_val_score(rf_regressor, X, y, cv=5, scoring='r2')
print("Random Forest Cross-Validation R² Scores:", rf_scores)
print("Mean CV R²:", rf_scores.mean())

# Prediction and Residual Analysis
rf_y_pred = rf_regressor.predict(X_test)
print("Random Forest R²:", r2_score(y_test, rf_y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, rf_y_pred))

# Residual Plot
residuals = y_test - rf_y_pred
sns.histplot(residuals, kde=True, bins=30, color='green')
plt.axvline(x=0, color='red', linestyle='--')
plt.title("Residual Distribution (Random Forest)")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

