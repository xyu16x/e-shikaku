from sklearn import datasets, linear_model
import matplotlib.pyplot as plt


def main():
    iris = datasets.load_iris()
    x = iris.data[:, 0]
    y = iris.data[:, 2]

    model = linear_model.LinearRegression()
    model.fit(x.reshape(-1, 1), y)

    plt.scatter(x, y)
    plt.plot(x, model.predict(x.reshape(-1, 1)))
    plt.show()
    plt.savefig("my_plot.png")


if __name__ == "__main__":
    main()
