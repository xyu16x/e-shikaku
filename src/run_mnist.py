import numpy as np
from tensorflow.keras.datasets import mnist


def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(x_train.shape)  # (60000,28,28)
    print(x_train.ndim)  # 3


if __name__ == "__main__":
    main()
