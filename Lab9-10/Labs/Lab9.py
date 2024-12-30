import numpy as np
import matplotlib.pyplot as plt

# Указанные значения alpha
alpha_values = [1, 20, 22, 23, 24.1, 24.5, 25, 25.5, 26, 28, 29]
# alpha_values = [1, 1.5, 2.22, 2.38, 2.43, 2.44, 2.46, 2.49, 2.50, 2.51, 2.6, 2.7, 2.82]
x_0 = 0.6  # Начальное условие
iterations = 1000
last = 100  # Количество точек для бифуркационной диаграммы


# Функция отображения
def f(x, alpha):
    return (1/7) * alpha * x * (1 - x)


# Применяемый диапазон alpha для бифуркационной диаграммы
alpha_range = np.linspace(0, 40, 10000)
x_values = []


for alpha in alpha_range:
    x = x_0
    for _ in range(iterations):
        x = f(x, alpha)
    for _ in range(last):  # Убираем начальные значения
        x = f(x, alpha)
        x_values.append((alpha, x))

# Преобразование в массив NumPy
x_values = np.array(x_values)

# Построение бифуркационной диаграммы
plt.figure(figsize=(10, 6))
plt.plot(x_values[:, 0], x_values[:, 1], ',k', alpha=0.4)
plt.title('Бифуркационная диаграмма')
plt.xlabel('$\\alpha$')
plt.ylabel('$x$')
plt.xlim(0, 28)
plt.grid()
plt.show()


for alpha in alpha_values:
    x_values = [x_0]
    for _ in range(iterations):
        x_values.append(f(x_values[-1], alpha))

    plt.plot(x_values, 'o', markersize=2)

    plt.title(f"Фазовый портрет при а = {alpha}")
    plt.xlabel("alpha")
    plt.ylabel("x")

    plt.show()