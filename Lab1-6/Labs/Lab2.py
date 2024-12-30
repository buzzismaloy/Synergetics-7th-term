import numpy as np
import matplotlib.pyplot as plt

def lab1_2():
    x = np.array([-5.1, -5.2, -5.3, -5.4, -5.5, -4.9, -4.8, -4.7, -4.8, -4.9])
    y = np.array([6.1, 6.9, 6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 6.2, 6.1])

    # First plot
    t = np.linspace(0, 5, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x1(x[i], t))
    plt.show()

    # Second plot
    t = np.linspace(0, 30, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x2(y[i], t))
    plt.show()

    # Third plot
    t = np.linspace(0, 10, 10000)
    plt.figure()
    for i in range(10):
        plt.plot(func_x1(x[i], t), func_x2(y[i], t))
    plt.show()

def func_x1(x_init, dt):
    x1 = [x_init]
    for i in range(len(dt) - 1):
         x1_next = (x1[i - 1] - 7 * dt[1]) / (1 - (2 / 3) * dt[1])
         x1.append(x1_next)
    return np.array(x1)

def func_x2(x_init, dt):
    x2 = [x_init]
    for i in range(len(dt) - 1):
        x2_next = (x2[i - 1] + 4 * dt[1]) / (1 - dt[1] / 3)
        x2.append(x2_next)
    return np.array(x2)

# Run the function
lab1_2()