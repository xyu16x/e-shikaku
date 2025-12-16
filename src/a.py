import numpy as np

# from tensorflow.keras.datasets import mnist


def newron():
    # w = np.array([[1, 2, 3], [2, 3, 4]])
    w = np.array([[3, 5], [4, 8]])
    x = np.array([[6], [9]])
    b = np.array([[4], [6]])
    # 2+6+12 = 20
    # 5+12+15=32
    # a = w.dot(x)
    res = w.dot(x) + b
    print(res)
    # my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # print(my_array)


def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y


def RSS(y, t):
    return 0.5 * (np.sum())


def mnist():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(x_train.shape)
    print(x_train.ndim)


if __name__ == "__main__":
    newron()
