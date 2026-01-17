import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

# 1. Load labeled data
df = pd.read_csv("data/labeled_overload_data.csv")

# 2. Features (X) and target (y)
X = df.drop("overload_score", axis=1)
y = df["overload_score"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train regression model
model = RandomForestRegressor(
    n_estimators=150,
    random_state=42,
    max_depth=None
)

model.fit(X_train, y_train)

# 5. Predictions
y_pred = model.predict(X_test)

# 6. Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("📊 Regression Evaluation")
print(f"MAE  (avg error): {mae:.2f}")
print(f"RMSE (spread)   : {rmse:.2f}")
print(f"R² score        : {r2:.3f}")

# 7. Save model
joblib.dump(model, "adhd_overload_regressor.pkl")
print("✅ Regression model saved as adhd_overload_regressor.pkl")

# 8. Feature importance
importances = model.feature_importances_
features = X.columns

print("\n🔍 Feature Importance:")
for feature, importance in sorted(zip(features, importances), key=lambda x: x[1], reverse=True):
    print(f"{feature:20s}: {importance:.3f}")
