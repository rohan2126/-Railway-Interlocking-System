import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_dataset(path='data/dataset.csv'):
    data = pd.read_csv(path)
    X = data.drop('collision', axis=1)
    y = data['collision']
    return X, y

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

def save_model(model, path='src/ai_model/train_model.pkl'):
    with open(path, 'wb') as file:
        pickle.dump(model, file)

def load_trained_model(path='src/ai_model/train_model.pkl'):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

if __name__ == "__main__":
    X, y = load_dataset()
    model = train_model(X, y)
    save_model(model)
    print("Model trained and saved successfully!")
