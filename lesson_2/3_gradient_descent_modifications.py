import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

args = 'x1 x2'
# Определяем символьные переменные
x1, x2 = sp.symbols(args)

# Запишем нашу функцию
function = x1 ** 2 + x2 ** 2

# Определим все производные нашей функции
df = {x: sp.diff(function, x) for x in args.split()}

# Зададим первую точку и шаг
a0 = (1, 2)
h = 0.1

# ------------------- Находим все координаты градиентного спуска ---------------

# ---------- Первая модификация ГС: с каждой итерацией уменьшаем шаг -----------
point = a0
points = (a0,)
t = 5
for n in range(t):
	h = h * (1 - n / t)
	# print(h)
	fx1 = sp.lambdify(x1, df['x1'])(point[0])
	fx2 = sp.lambdify(x2, df['x2'])(point[1])
	point = point[0] - h * fx1, point[1] - h * fx2
	points += point,
	if abs(fx1) < 0.008 > abs(fx2):
		break

# print(*points, sep='\n')


# --------- Вторая модификация ГС "Adagrad": каждый градиент умножаем на свой Шаг ---------
point = a0
points = (a0,)
t = 40
G = [0, 0]		#
for n in range(t):
	fx1 = sp.lambdify(x1, df['x1'])(point[0])
	fx2 = sp.lambdify(x2, df['x2'])(point[1])
	G[0] += fx1 ** 2
	G[1] += fx2 ** 2
	point = (
			point[0] - h / (G[0] ** 0.5 + 0.001) * fx1,
			point[1] - h / (G[1] ** 0.5 + 0.001) * fx2
			)
	points += point,
	if abs(fx1) < 0.008 > abs(fx2):
		break

# print(*points, sep='\n')


# --------- Третий метод ГС "Adam": каждый градиент умножаем на свой Шаг ---------
point = a0
points = (a0,)
e = 0.001				# Константа, близкая к 0
bm, br = 0.9, 0.999		# Константа (обычно близкая к 1)
t = 20					# Количество итераций
m = [0, 0]				# Переменная для расчета M
r = [0, 0]				# Переменная для расчета R
M = [0, 0]				# градиенты с прошлого шага
R = [0, 0]				# квадраты градиентов с прошлого шага
for step in range(1, t):
	fx1 = sp.lambdify(x1, df['x1'])(point[0])
	fx2 = sp.lambdify(x2, df['x2'])(point[1])
	m = [bm * m[0] + (1 - bm) * fx1, bm * m[1] + (1 - bm) * fx2]
	r = [br * r[0] + (1 - br) * fx1 ** 2, br * r[1] + (1 - br) * fx2 ** 2]
	M = [m[0] / (1 - bm ** step), m[1] / (1 - bm ** step)]
	R = [r[0] / (1 - br ** step), r[1] / (1 - br ** step)]
	point = (
			point[0] - h * M[0] / (R[0] + e) ** 0.5,
			point[1] - h * M[1] / (R[1] + e) ** 0.5
			)
	points += point,
	if abs(fx1) < 0.008 > abs(fx2):
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
#plt.show()
