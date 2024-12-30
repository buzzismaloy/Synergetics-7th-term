import numpy as np
import matplotlib.pyplot as plt

def lab1_1():
    x = np.array([4, 5, 6, 7, 8, -4, -5, -6, -7, -8])
    y = np.array([5, 6, 7, 8, 9, -5, -6, -7, -8, -9])
    # First plot
    t = np.linspace(0, 10, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x1(x[i], t))
    plt.show()

    # Second plot
    t = np.linspace(0, 30, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x2(y[i], func_x1(x[i], t), t))
    plt.show()

    # Third plot
    t = np.linspace(0, 10, 10000)
    plt.figure()
    for i in range(10):
        plt.plot(func_x1(x[i], t), func_x2(y[i], func_x1(x[i], t), t))
    plt.show()

def func_x1(x_init, dt):
    x1 = np.zeros(len(dt))
    x1[0] = x_init
    for i in range(1, len(dt)):
        x1[i] = x1[i - 1] + dt[1] * 3 - ((2 / 3) * x1[i - 1] * dt[1])
    return x1

def func_x2(x_init, x1, dt):
    x2 = np.zeros(len(dt))
    x2[0] = x_init
    for i in range(1, len(dt)):
        x2[i] = x2[i - 1] - 4.5 * x2[i - 1] * dt[1] + 0.5 * x1[i - 1] * dt[1]
    return x2

# Run the function
lab1_1()
