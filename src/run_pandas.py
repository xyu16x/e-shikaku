import pandas as pd
import numpy as np


def main():
    data = pd.DataFrame(
        {
            "col1": [1, 2, None, np.nan],
            "col2": [1.2, 2.3, None, np.nan],
            "col3": ["aaa", "bbb", None, np.nan],
        }
    )
    print(data)
    print(data.isna())
    print(data.dropna())

    s = pd.Series([3, 2, 3, 2, 2])
    s2 = pd.Series([2, 4, 6, 8, 10])

    print(s)
    print(s2)

    df = pd.concat([s, s2], axis=1)
    print(df)
    print(type(df))


if __name__ == "__main__":
    main()
