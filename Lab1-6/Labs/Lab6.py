import numpy as np
import matplotlib.pyplot as plt

def func_x(x1_init, x2_init, dt):
    x = np.zeros((2, len(dt)))
    x[0, 0] = x1_init
    x[1, 0] = x2_init

    for i in range(len(dt) - 1):
        x[1, i + 1] = (0.5 * x[0, i] + 11 * dt[1] + x[1, i]) / (1 - 3 * dt[1])
        x[0, i + 1] = 3 * dt[1] * x[0, i] - 2 * dt[1] * x[1, i + 1] - 14 * dt[1] + x[0, i]

    return x

def lab1_6():
    x = np.array([0.01, 0.02, 0.03, 0.04, 0.05, -0.01, -0.02, -0.03, -0.04, -0.05])
    y = np.array([-2.49, -2.48, -2.47, -2.46, -2.45, -2.51, -2.52, -2.53, -2.54, -2.55])

    # Первая фигура
    t = np.linspace(0, 100, 10000)
    plt.figure()
    for i in range(10):
        tmp = func_x(x[i], y[i], t)
        plt.plot(t, tmp[0, :], label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("График x[0] от t")
    plt.xlabel("t")
    plt.ylabel("x[0]")
    plt.legend()

    # Вторая фигура
    t = np.linspace(0, 100, 100)
    plt.figure()
    for i in range(10):
        tmp = func_x(x[i], y[i], t)
        plt.plot(t, tmp[1, :], label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("График x[1] от t")
    plt.xlabel("t")
    plt.ylabel("x[1]")
    plt.legend()

    # Третья фигура
    t = np.linspace(0, 5, 5000)
    plt.figure()
    for i in range(10):
        tmp = func_x(x[i], y[i], t)
        plt.plot(tmp[0, :], tmp[1, :], label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("Параметрический график x[0] и x[1]")
    plt.xlabel("x[0]")
    plt.ylabel("x[1]")
    plt.legend()

    plt.show()

# Запуск функции
lab1_6()
