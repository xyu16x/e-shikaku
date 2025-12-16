import seaborn as sns


def main(x):
    iris = sns.load_dataset("iris")
    type(iris)
    sns.pairplot("sepal_width", "petal_length", data=iris)


if __name__ == "__main__":
    main()
