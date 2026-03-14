import pennylane as qml
from pennylane import numpy as np

def optimize(cost_fn, params, features, dev, steps=30):
    opt = qml.GradientDescentOptimizer(stepsize=0.1)
    history = []
    for it in range(steps):
        params = opt.step(lambda v: cost_fn(v, features, dev), params)
        history.append(cost_fn(params, features, dev))
    return params, history