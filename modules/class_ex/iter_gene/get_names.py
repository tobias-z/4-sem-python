import pandas as pd


def get_names():
    with open("files/navne.csv") as file:
        for name in file:
            yield name.split("\n")[0]


if __name__ == "__main__":
    names = get_names()
    print(next(names))
    print(next(names))
