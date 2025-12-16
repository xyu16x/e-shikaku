import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split as tts


def main(x):
    return np.sin(2 * np.pi * x)


if __name__ == "__main__":
    sin_x = np.linspace(0, 1, 100)
    x = np.random.rand(100)[:, np.newaxis]
    y = main(x) + np.random.rand(100)[:, np.newaxis] - 0.5
    x_train, x_test, y_train, y_test = tts(x, y)
    plt.plot(sin_x, main(sin_x), ":")
    plt.show()
