# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Example dataset
data = {
    'area': [1000, 1500, 2000, 2500, 3000],
    'price': [100000, 150000, 200000, 250000, 300000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['area']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'house_price_model.pkl')
print("✅ Model trained and saved as house_price_model.pkl")
