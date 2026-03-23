# QUANTUM: QFT & Variational Quantum Algorithms

A specialized quantum computing repository focused on the implementation, optimization, and visualization of Quantum Fourier Transforms (QFT) and variational quantum circuits.

---

##  Project Structure

* **`src/`**: The core quantum logic directory.
    * `qft_exact.py`: Standard mathematical implementation of the QFT.
    * `qft_variational.py`: Parameterized circuits for variational QFT approximation.
    * `encoding.py`: Logic for mapping classical data into quantum states (Amplitude/Angle encoding).
    * `optimizer.py`: Classical optimization routines for tuning quantum parameters.
    * `cost_function.py`: Definition of objective functions for variational training.
    * `visualization.py`: Tools for generating circuit diagrams and probability distributions.
* **`data/`**: Contains `preprocess.py` for preparing input data for quantum processing.
* **`app.py`**: The entry point for the application interface.
* **`main.py`**: The primary script for executing experiments and simulations.
* **`qft_env/`**: Local virtual environment folder.
* **`requirements.txt`**: Project dependencies and framework versions.

---

##  Getting Started

### 1. Environment Activation
It is recommended to use the existing `qft_env` virtual environment:

```bash
# For Windows:
qft_env\Scripts\activate

# For Mac/Linux:
source qft_env/bin/activate

# Install required packages
pip install -r requirements.txt
