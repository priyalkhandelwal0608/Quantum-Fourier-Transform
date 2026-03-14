import pennylane as qml

def variational_qft(params, features, wires):
    from .encoding import encode_features
    encode_features(features, wires)
    for i, w in enumerate(wires):
        qml.RY(params[i], wires=w)
    qml.CNOT(wires=[wires[0], wires[1]])
    qml.RZ(params[2], wires=wires[1])