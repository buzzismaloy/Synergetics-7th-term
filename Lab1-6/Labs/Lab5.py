import numpy as np
import matplotlib.pyplot as plt

def func_x1(x1_init, x2_init, dt):
    x1 = [x1_init]
    x2 = [x2_init]
    for i in range(len(dt) - 1):
        x1_next = ((-3 / 7) * dt[1] * x2[i] + 11 * dt[1] + x1[i]) / (1 + 2 * dt[1])
        x2_next = ((7 /4) * dt[1] * x1[i] + 7 * dt[1] + x2[i]) / (1 + 2 * dt[1])
        x1.append(x1_next)
        x2.append(x2_next)
    return np.array(x1)

def func_x2(x2_init, x1_init, dt):
    x2 = [x2_init]
    x1 = [x1_init]
    for i in range(len(dt) - 1):
        x1_next = ((-3 / 7) * dt[1] * x2[i] + 11 * dt[1] + x1[i]) / (1 + 2 * dt[1])
        x2_next = ((7 /4) * dt[1] * x1[i] + 7 * dt[1] + x2[i]) / (1 + 2 * dt[1])
        x1.append(x1_next)
        x2.append(x2_next)
    return np.array(x2)

def lab1_5():
    x = np.array([10, 11, 12, 13, 14, -12, -13, -14, -15, -16])
    y = np.array([13, 14, 15, 16, 17, -7, -8, -9, -10, -11])

    # Первая фигура
    t = np.linspace(0, 10, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x1(x[i], y[i], t), label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("График func_x1 от t")
    plt.xlabel("t")
    plt.ylabel("func_x1")
    plt.legend()

    # Вторая фигура
    t = np.linspace(0, 30, 1000)
    plt.figure()
    for i in range(10):
        plt.plot(t, func_x2(y[i], x[i], t), label=f"y[{i}], x[{i}]")
    plt.grid(True)
    plt.title("График func_x2 от t")
    plt.xlabel("t")
    plt.ylabel("func_x2")
    plt.legend()

    # Третья фигура
    t = np.linspace(0, 30, 10000)
    plt.figure()
    for i in range(10):
        plt.plot(func_x1(x[i], y[i], t), func_x2(y[i], x[i], t), label=f"x[{i}], y[{i}]")
    plt.grid(True)
    plt.title("Параметрический график func_x1 и func_x2")
    plt.xlabel("func_x1")
    plt.ylabel("func_x2")
    plt.legend()

    plt.show()

# Запуск функции
lab1_5()