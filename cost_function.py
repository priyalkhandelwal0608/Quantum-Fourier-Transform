import pennylane as qml
import numpy as np
from .qft_exact import qft_matrix
from .qft_variational import variational_qft

def make_qnode(dev):
    wires = dev.wires  # use wires directly
    @qml.qnode(dev)
    def circuit(params, features):
        variational_qft(params, features, wires=wires)
        return qml.state()
    return circuit

def cost(params, features, dev):
    wires = dev.wires
    circuit = make_qnode(dev)
    state_var = circuit(params, features)

    N = 2**len(wires)
    qft = qft_matrix(N)

    # exact state
    @qml.qnode(dev)
    def exact(features):
        qml.AngleEmbedding(features, wires=wires)
        return qml.state()
    state_exact = exact(features)
    qft_exact = qft @ state_exact

    return 1 - np.abs(np.dot(np.conj(qft_exact), state_var))**2