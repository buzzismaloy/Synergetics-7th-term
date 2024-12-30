import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры
sigma = 4
b = 2

r_values = [10, 28, 40]
initial_conditions = (0.0001, 0, 0)
t = np.linspace(0, 40, 1000)

fig, axs = plt.subplots(1, 2, figsize=(15, 5))  # 1 строка, 4 столбца


# Система уравнений Лоренца
def lorenz(X, t, r):
    x, y, z = X
    dx = sigma * (y - x)
    dy = r * x - y - x * z
    dz = x * y - b * z
    return [dx, dy, dz]


# Численное исследование системы Лоренца
def solve_lorenz(r, initial_conditions, t):
    return odeint(lorenz, initial_conditions, t, args=(r,))


# Построим фазовые портреты
def plot_phase_portraits(r_values, initial_conditions, t):
    for r in r_values:
        sol = solve_lorenz(r, initial_conditions, t)
        axs[0].plot(sol[:, 0], sol[:, 2], label=f'r = {r}')

    axs[0].axvline(-9/16, color='red', linestyle='--', label='Точка бифуркации (a = 0)')
    axs[0].axvline(1, color='red', linestyle='--', label='Точка бифуркации (a = 0)')

    axs[0].set_xlabel('x')
    axs[0].set_ylabel('z')
    axs[0].set_title('Фазовые портреты системы Лоренца')
    axs[0].legend()


# Исследуем расхождение траекторий в области хаоса
def investigate_chaos(r, initial_conditions1, initial_conditions2, t):
    sol1 = solve_lorenz(r, initial_conditions1, t)
    sol2 = solve_lorenz(r, initial_conditions2, t)
    d = np.sqrt((sol1[:, 0] - sol2[:, 0])**2 + (sol1[:, 1] - sol2[:, 1])**2 + (sol1[:, 2] - sol2[:, 2])**2)
    axs[1].plot(t, d)
    axs[1].set_xlabel('t')
    axs[1].set_ylabel('d(t)')
    axs[1].set_title('Расхождение траекторий в области хаоса')


# Построим фазовые портреты
plot_phase_portraits(r_values, initial_conditions, t)

# Исследуем расхождение траекторий в области хаоса
r_chaos = 28
initial_conditions1 = (0.0001, 0, 0)
initial_conditions2 = (0.0001, 0, 1e-12)
investigate_chaos(r_chaos, initial_conditions1, initial_conditions2, t)

# Автоматическая корректировка отступов
plt.tight_layout()
plt.show()