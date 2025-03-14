from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

class FinTechLLM:
    def __init__(self, model_name="facebook/opt-1.3b"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def predict_sentiment(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=50)
        return self.tokenizer.decode(outputs[0])

class MarketPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.scaler = StandardScaler()

    def train(self, X_train, y_train):
        X_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_scaled, y_train)

    def predict(self, X_test):
        X_scaled = self.scaler.transform(X_test)
        return self.model.predict(X_scaled)

    def save_model(self, filename="market_predictor.pkl"):
        joblib.dump((self.model, self.scaler), filename)

    def load_model(self, filename="market_predictor.pkl"):
        self.model, self.scaler = joblib.load(filename)

class FraudDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, filename="fraud_detector.pkl"):
        joblib.dump(self.model, filename)

    def load_model(self, filename="fraud_detector.pkl"):
        self.model = joblib.load(filename)

class PortfolioOptimizer:
    def __init__(self):
        pass

    def optimize_portfolio(self, returns):
        mean_returns = np.mean(returns, axis=0)
        return mean_returns / np.std(mean_returns) 