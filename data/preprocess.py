from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

def load_and_preprocess():
    iris = load_iris()
    X = iris.data
    y = iris.target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled[:, :2], y   # reduce to 2 features
