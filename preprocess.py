import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def preprocess_and_train():
    # Load dataset
    df = pd.read_csv('dataset.csv')

    # Features and label
    X = df.drop('Condition', axis=1)
    y = df['Condition']

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Save model
    joblib.dump(model, 'model/disease_predictor.pkl')
    print("Model trained and saved to model/disease_predictor.pkl")

if __name__ == '__main__':
    preprocess_and_train()
