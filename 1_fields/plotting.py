import matplotlib.pyplot as plt
import numpy as np

L_EYE = 2 + 2j
R_EYE = 3 + 2j
MOUTH = [r + 1j for r in np.linspace(1.75, 3.25, num=7)]
S = [L_EYE] + [R_EYE] + MOUTH



def plot(a, lim, **kwargs):
    reals = [x.real for x in a]
    imags = [x.imag for x in a]
    plt.scatter(reals, imags, **kwargs)
    plt.xlim([-lim, lim])
    plt.ylim([-lim, lim])
    plt.plot([-lim, lim], [0, 0], 'k-', alpha=0.5)
    plt.plot([0, 0], [-lim, lim], 'k-', alpha=0.5)
    plt.show()



if __name__ == '__main__':
    plot(S, 4)

