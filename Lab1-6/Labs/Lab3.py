import numpy as np
import matplotlib.pyplot as plt

def func_x1(x_init, dt):
    x1 = [x_init]
    for i in range(len(dt) - 1):
        x1_next = (x1[i] + dt[1]) / (1 + dt[1] / 6)
        x1.append(x1_next)
    return np.array(x1)

def func_x2(x_init, dt):
    x2 = [x_init]
    for i in range(len(dt) - 1):
        x2_next = x2[i] + dt[1] * 7 * x2[i] / 4
        x2.append(x2_next)
    return np.array(x2)

def lab1_3():
    x = np.array([10, 11, 12, 13, 14, -10, -11, -12, -13, -14])
    y = np.array([13, 14, 15, 16, 17, -7, -8, -9, -10, -11])

    # Первая фигура
    t = np.linspace(0, 10, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x1(x[i], t), label=f"x[{i}]")
    plt.grid(True)
    plt.title("График func_x1 от t")
    plt.xlabel("t")
    plt.ylabel("func_x1")
    plt.legend()

    # Вторая фигура
    t = np.linspace(0, 5, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x2(y[i], t), label=f"y[{i}]")
    plt.grid(True)
    plt.title("График func_x2 от t")
    plt.xlabel("t")
    plt.ylabel("func_x2")
    plt.legend()

    # Третья фигура
    t = np.linspace(0, 3, 10000)
    plt.figure()
    for i in range(10):
        plt.plot(func_x1(x[i], t), func_x2(y[i], t), label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("Параметрический график func_x1 и func_x2")
    plt.xlabel("func_x1")
    plt.ylabel("func_x2")
    plt.legend()

    plt.show()

# Запуск функции
lab1_3()