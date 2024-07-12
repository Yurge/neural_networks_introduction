import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

args = 'x1 x2'
# Определяем символьные переменные
x1, x2 = sp.symbols(args)

# Запишем нашу функцию
function = x1 ** 2 + 10 * x2 ** 2

# Определим все производные нашей функции
df = {x: sp.diff(function, x) for x in args.split()}

# Зададим первую точку и шаг
a0 = (10, 1)
h = 0.1

# Находим все координаты градиентного спуска
point = a0
points = (a0,)
for _ in range(20):
	fx1 = sp.lambdify(x1, df['x1'])(point[0])
	fx2 = sp.lambdify(x2, df['x2'])(point[1])
	point = ((point[0] - h * fx1), (point[1] - h * fx2))
	points += point,
	if abs(fx1) < 0.008:
		break


# Построение графика функции
x_vals = np.linspace(-11, 11, 100)
y_vals = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x_vals, y_vals)
z = x**2 + 10*y**2
fig = plt.figure(figsize=(7, 7))
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, alpha=0.7)

# Координаты градиентного спуска
x_grad = [elem[0] for elem in points]
y_grad = [elem[1] for elem in points]
z_grad = [x ** 2 + 10 * y ** 2 for x, y in zip(x_grad, y_grad)]
ax.scatter(x_grad, y_grad, z_grad, color='red')

# Вывод графика на экран
plt.show()
