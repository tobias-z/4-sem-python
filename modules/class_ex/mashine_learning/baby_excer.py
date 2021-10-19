from enum import Enum
import random
import csv
from typing import List
import matplotlib.pyplot as plt

BABY_FILE = "files/babies.csv"


class Gender(Enum):
    MALE = 0
    FEMALE = 1


class Baby:
    def __init__(self, gender: Gender, height: float, weight: float) -> None:
        self.gender = gender
        self.height = height
        self.weight = weight


def generate_babies(amount: int):
    with open(BABY_FILE, "w") as f:
        f.write("GENDER, HEIGHT, WEIGHT\n")
        for _ in range(0, amount):
            baby = Baby(
                random.choice([Gender.MALE, Gender.FEMALE]),
                random.choice(range(10, 60)),
                random.choice(range(0, 100)),
            )
            f.write(f"{baby.gender.value}, {baby.height}, {baby.weight}\n")


def plot_babies(babies: List[Baby]):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    x = [baby.gender for baby in babies]
    y = [baby.weight for baby in babies]
    z = [baby.height for baby in babies]
    ax.scatter(x, y, z, linewidth=0.2)


def read_babies():
    babies: List[Baby] = []
    with open(BABY_FILE, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        for row in reader:
            babies.append(Baby(row[0], row[1], row[2]))

    plot_babies(babies)


if __name__ == "__main__":
    generate_babies(10)
