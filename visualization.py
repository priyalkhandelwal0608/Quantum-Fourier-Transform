import matplotlib.pyplot as plt

def plot_history(history):
    plt.plot(history, label="Cost")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.legend()
    plt.show()