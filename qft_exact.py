import numpy as np

def qft_matrix(N):
    omega = np.exp(2j * np.pi / N)
    return np.array([[omega**(i*j) for j in range(N)] for i in range(N)]) / np.sqrt(N)