import matplotlib.pyplot as plt
import numpy as np

def calc_x(x1, x2, t, dt, alpha):
    x1_n_1 = np.zeros_like(t)
    x1_n_1[0] = x1
    x2_n_1 = np.zeros_like(t)
    x2_n_1[0] = x2

    for i in range(1, len(t)):
        x1_n_1[i] = x1_n_1[i - 1] + dt * (9 * alpha * x1_n_1[i - 1] - x2_n_1[i - 1] - 0.2 * x1_n_1[i - 1] * (x1_n_1[i - 1] * x1_n_1[i - 1] + x2_n_1[i - 1] * x2_n_1[i - 1]))
        x2_n_1[i] = x2_n_1[i - 1] + dt * (x1_n_1[i - 1] + 9 * alpha * x2_n_1[i - 1] - 0.2 * x2_n_1[i - 1] * (x1_n_1[i - 1] * x1_n_1[i - 1] + x2_n_1[i - 1] * x2_n_1[i - 1]))
    return np.array([x1_n_1, x2_n_1])


def main():
    x1 = np.array([-3, -3, 3, 3, -3, 3, 0, 10, -10, 10, -10])
    x2 = np.array([-3, 3, -3, 3, 0, 0, -3, 10, 10, -10, -10])
    alphas = np.array([-1, -1/5, 5])

    start, stop, num = 0, 10, 1000

    t = np.linspace(start, stop, num)
    dt = stop / num


    plt.scatter(0, 0, s=20)


    for i in range(len(x1)):
        x = calc_x(x1[i], x2[i], t, dt, alphas[0])
        plt.plot(x[0, :], x[1, :])
    plt.grid(True)
    plt.show()


    for i in range(len(x1)):
        x = calc_x(x1[i], x2[i], t, dt, alphas[1])
        plt.plot(x[0, :], x[1, :])
    plt.grid(True)
    plt.show()


    x1 = np.array([-0.01, -0.01, 0.01, 0.01, -0.01, 0.01, 0, 10, -10, 10, -10])
    x2 = np.array([-0.01, 0.01, -0.01, 0.01, 0, 0, -0.01, 0.01, 10, 10, -10, -10])

    for i in range(len(x1)):
        x = calc_x(x1[i], x2[i], t, dt, alphas[2])
        plt.plot(x[0, :], x[1, :])
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()

