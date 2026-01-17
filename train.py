import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load dataset
df = pd.read_csv("data/overload_log.csv")

# 2. Separate features (X) and target (y)
X = df.drop("overload_level", axis=1)
y = df["overload_level"]

# 3. Encode labels (Low / Medium / High → numbers)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# 5. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Save model and encoder
joblib.dump(model, "adhd_overload_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("✅ Model and encoder saved successfully")
