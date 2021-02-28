import matplotlib.pyplot as plt
import numpy as np

L_EYE = 2 + 2j
R_EYE = 3 + 2j
MOUTH = [r + 1j for r in np.linspace(1.75, 3.25, num=7)]
S = [L_EYE] + [R_EYE] + MOUTH


def plot(S: list[complex], lim, **kwargs):
    reals = [x.real for x in S]
    imags = [x.imag for x in S]
    plt.scatter(reals, imags, **kwargs)
    plt.xlim([-lim, lim])
    plt.ylim([-lim, lim])
    plt.plot([-lim, lim], [0, 0], 'k-', alpha=0.5)
    plt.plot([0, 0], [-lim, lim], 'k-', alpha=0.5)
    plt.show()


def translate(S: list[complex], z: complex) -> list[complex]:
    return [x + z for x in S]


def scale(S: list[complex], k) -> list[complex]:
    return [k * x for x in S]


def rotate90(S: list[complex]) -> list[complex]:
    return [(0 + 1j) * x for x in S]
    


if __name__ == '__main__':
    plot(S, 5)
    plot(translate(S, 1 + 2j), 5)
    plot(scale(S, 1/2), 5)
    plot(rotate90(S), 5)

