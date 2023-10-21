import numpy as np


def main():
    x = [1, 1]
    w = np.array([1, 1])
    print(x * w)
    sum = np.sum(x * w)
    print(sum)
    print(sum + -1.5)


main()
