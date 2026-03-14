from data.preprocess import load_and_preprocess
from src.cost_function import cost
from src.optimizer import optimize
from src.visualization import plot_history
import pennylane as qml
from pennylane import numpy as np

def main():
    # Load dataset
    X, y = load_and_preprocess()
    features = X[0]   # take one sample

    # Device
    dev = qml.device("default.qubit", wires=2)

    # Initialize params
    params = np.random.uniform(0, np.pi, 3)

    # Optimize
    params, history = optimize(cost, params, features, dev, steps=30)

    # Visualize
    plot_history(history)

if __name__ == "__main__":
    main()