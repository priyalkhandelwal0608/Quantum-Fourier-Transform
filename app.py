import streamlit as st
import pandas as pd
import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

from data.preprocess import load_and_preprocess
from src.cost_function import cost
from src.optimizer import optimize

# --- App Header ---
st.set_page_config(page_title="Quantum QFT App", layout="centered")
st.title("⚛️ Quantum Fourier Transform with Variational Circuits")
st.markdown("""
Welcome to the **Quantum QFT App**.  
You can either run a demo with the Iris dataset, upload your own dataset, or download a sample dataset to try.
""")

# --- Dataset Options ---
mode = st.radio("Choose Mode:", ["Run Demo", "Upload Dataset"])

features = None

if mode == "Run Demo":
    st.info("Demo mode uses the Iris dataset (2 features).")
    X, y = load_and_preprocess()
    sample_index = st.slider("Select Sample Index", 0, len(X)-1, 0)
    features = X[sample_index]

else:
    uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if df.shape[1] < 2:
                st.error("❌ Invalid dataset: must have at least 2 numeric columns.")
            else:
                st.success("✅ Dataset uploaded successfully.")
                features = df.iloc[0, :2].values
        except Exception as e:
            st.error(f"❌ Error reading dataset: {str(e)}")
    else:
        st.warning("Please upload a dataset to continue.")

# --- Download Sample Dataset ---
sample_df = pd.DataFrame({
    "feature1": [0.1, 0.2, 0.3],
    "feature2": [0.5, 0.6, 0.7]
})
st.download_button(
    label="📥 Download Sample Dataset",
    data=sample_df.to_csv(index=False),
    file_name="sample_dataset.csv",
    mime="text/csv"
)

# --- Optimization Section ---
if features is not None:
    st.subheader("🔧 Optimization Settings")
    steps = st.slider("Optimization Steps", 10, 100, 30)

    dev = qml.device("default.qubit", wires=2)
    params = np.random.uniform(0, np.pi, 3)

    params, history = optimize(cost, params, features, dev, steps=steps)

    st.subheader("📊 Results")
    fig, ax = plt.subplots()
    ax.plot(history, label="Cost")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Cost")
    ax.legend()
    st.pyplot(fig)

    st.write("**Optimized Parameters:**", params)