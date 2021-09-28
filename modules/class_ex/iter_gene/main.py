from get_names import get_names


def get_some_names(amount: int):
    gene = get_names()
    return [next(gene) for _ in range(0, amount)]


if __name__ == "__main__":
    print(get_some_names(10))
