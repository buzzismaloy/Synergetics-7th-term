import matplotlib.pyplot as plt
import numpy as np

def calc_x1(x_n, t, dt, alpha):
    x_n_1 = np.zeros_like(t)
    x_n_1[0] = x_n

    for i in range(1, len(t)):
        x_n_1[i] = x_n_1[i - 1] + dt * (x_n_1[i - 1] * x_n_1[i - 1] - 6 * x_n_1[i-1] + 3 * alpha / 2)
    return x_n_1


def calc_x2(x2_n, x1_n, t, dt, alpha):
    x2_n_1 = np.zeros_like(t)
    x2_n_1[0] = x2_n

    for i in range(1, len(t)):
        x2_n_1[i] = x2_n_1[i - 1] + dt * (x1_n[i - 1] - x2_n_1[i - 1] + alpha / 3)
    return x2_n_1


def main():
    x1 = np.array([-6, -6, 1.01, 1.09, 1.79, 1.51])
    x2 = np.array([-6, 6, 2.49, -9, -9, 2.51])
    alphas = [-0.75, 0, 0.3, 2]
    plt.xlim(-10, 15)
    plt.ylim(-20, 20)

    start, stop, num = 0, 10, 1000

    t = np.linspace(start, stop, num)
    dt = stop / num

    plt.scatter(np.sqrt(-3 * alphas[0]), -np.sqrt(-3 * alphas[0]) - 1, s=20)
    plt.scatter(-np.sqrt(-3 * alphas[0]), np.sqrt(-3 * alphas[0]) - 1, s=20)

    plt.xlim(-10, 15)
    plt.ylim(-20, 20)
    plt.scatter(np.sqrt(-3 * alphas[0]), -np.sqrt(-3 * alphas[0]) - 1, s=20)
    plt.scatter(-np.sqrt(-3 * alphas[0]), np.sqrt(-3 * alphas[0]) - 1, s=20)

    for i in range(len(x1)):
        x1_n = calc_x1(x1[i], t, dt, alphas[0])
        x2_n = calc_x2(x2[i], x1_n, t, dt, alphas[0])
        plt.plot(x1_n, x2_n)
    plt.grid(True)
    plt.show()

    plt.xlim(-10, 15)
    plt.ylim(-20, 20)
    plt.scatter(np.sqrt(-3 * alphas[1]), -np.sqrt(-3 * alphas[1]) - 1, s=20)
    plt.scatter(-np.sqrt(-3 * alphas[1]), np.sqrt(-3 * alphas[1]) - 1, s=20)

    for i in range(len(x1)):
        x1_n = calc_x1(x1[i], t, dt, alphas[1])
        x2_n = calc_x2(x2[i], x1_n, t, dt, alphas[1])
        plt.plot(x1_n, x2_n)
    plt.grid(True)
    plt.show()

    plt.xlim(-10, 15)
    plt.ylim(-20, 20)

    for i in range(len(x1)):
        x1_n = calc_x1(x1[i], t, dt, alphas[2])
        x2_n = calc_x2(x2[i], x1_n, t, dt, alphas[2])
        plt.plot(x1_n, x2_n)
    plt.grid(True)
    plt.show()


    alphas_scatters = np.linspace(-10, 0, 1000)
    plt.xlim(-10, 0)
    x1, x2, x3, x4 = list(), list(), list(), list()

    for i in range(len(alphas_scatters)):
        x1.append(np.sqrt(-3 * alphas_scatters[i]))
        x2.append(-np.sqrt(-3 * alphas_scatters[i]) - 1)
        x3.append(-np.sqrt(-3 * alphas_scatters[i]))
        x4.append(np.sqrt(-3 * alphas_scatters[i]) - 1)
    plt.plot(alphas_scatters, x1)
    plt.plot(alphas_scatters, x2)
    plt.plot(alphas_scatters, x3)
    plt.plot(alphas_scatters, x4)
    plt.show()

if __name__ == '__main__':
    main()
