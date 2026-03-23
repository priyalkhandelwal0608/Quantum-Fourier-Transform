import pennylane as qml

def encode_features(features, wires):
    qml.AngleEmbedding(features, wires=wires)