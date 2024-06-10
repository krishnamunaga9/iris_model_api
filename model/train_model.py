# model/train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model():
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Train a RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    #  Save the model to a file
    with open("model/model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_and_save_model()
