import matplotlib.pyplot as plt
import numpy as np

def plot_time_series(Y, x=None, title=None, xlabel='Year', ylabel='Value', 
                    style='b-', figsize=(10, 6)):
    time_steps = x if x is not None else np.arange(2020, 2020 + len(Y)*10, 10)

    plt.figure(figsize=figsize)
    plt.plot(time_steps, Y, style, label=ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()
    
    plt.close() 