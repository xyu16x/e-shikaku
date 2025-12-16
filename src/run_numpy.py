import numpy as np

# from tensorflow.keras.datasets import mnist


def main():
    x = np.array([[1, 2], [3, 4]])
    w = np.array([[8, 7], [6, 5]])

    res = x.dot(w)
    print(res)


if __name__ == "__main__":
    main()
