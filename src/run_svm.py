from sklearn import datasets
from sklearn import svm


def main():
    digits = datasets.load_digits()
    dataset = digits.data
    target = digits.target

    train_dataset = dataset[:-10]
    train_target = target[:-10]

    test_dataset = dataset[-10:]
    test_target = target[-10:]

    clf = svm.SVC(gamma=0.001, C=100)
    clf.fit(train_dataset, train_target)
    clf.predict(test_dataset)


if __name__ == "__main__":
    main()
