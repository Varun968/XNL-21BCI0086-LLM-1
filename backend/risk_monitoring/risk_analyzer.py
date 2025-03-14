from sklearn.ensemble import RandomForestClassifier
import numpy as np

X_train = np.array([[0.5, 1000, 0.1], [2.1, 500, 0.3], [1.2, 700, 0.2]])
y_train = np.array([0, 1, 1])  

model = RandomForestClassifier()
model.fit(X_train, y_train)

new_trade = np.array([[1.5, 600, 0.25]])
risk_prediction = model.predict(new_trade)
print("Risk Level:", "High" if risk_prediction[0] else "Low")
