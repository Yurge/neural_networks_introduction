import random
from sympy import symbols, diff, lambdify, ln, E


# ------------------------------------- Генеративно-состязательные сети (GAN) -------------------------------------


# Все отрицательные значения - это фейк, а все положительные - это true.
# Деструктор должен научиться определять фейк и true, а генератор должен понять, что выдавать в деструктор нужно
# только положительные числа. Исходя из этого Деструктор и Генератор меняют свои веса.

# Определяем символьные переменные
w, b, u, d = symbols('w, b, u, d', real=True)

# случайные числа для Генератора
# r = random.sample(range(-10, -1), 2)
r = [-1, -2]

# Зададим первую точку и шаг
a0 = (1, 0, 0, 0)		# w, b, u, d
h = 0.1

# функция Генератора
G = lambda r, w=a0[0], b=a0[1]: w * r + b

# Функция Активации = сигмоида. Переводит аргумент в вероятность в интервале от 0 до 1
f_sigm = lambda elem: 1 / (1 + E ** -elem)
# функция для округления
R = lambda x: round(x, 3)



# входные и целевые данные ТВ для Деструктора
x_val, y_val = [G(r[0]), G(r[1]), 1], [0, 0, 1]

# функция Деструктора
D = lambda x: f_sigm(x * u + d)
# функция потерь для Деструктора
F_D = sum([ln(1 - y - D(x)) for x, y in zip(x_val, y_val)])
# находим производные
u_diff = diff(F_D, u)
d_diff = diff(F_D, d)

# функция потерь для Генератора
F_G = sum([ln(f_sigm((w * x + b) * u + d)) for x in r])
# находим производные
w_diff = diff(F_G, w)
b_diff = diff(F_G, b)

# сам ГС
point = a0		# w, b, u, d
points = (a0,)
for _ in range(1):
	# Сначала находим новые значения Деструктора (u, d)
	ldf_ud = lambdify((u, d), expr=u_diff)(u=point[2], d=point[3])
	ldf_dd = lambdify((u, d), expr=d_diff)(u=point[2], d=point[3])
	u_new, d_new = R(point[2] - h * ldf_ud), R(point[3] - h * ldf_dd)
	# Затем находим новые значения Генератора (w, b)
	ldf_wd = lambdify((w, b, u, d), expr=w_diff)(w=point[0], b=point[1], u=u_new, d=d_new)
	ldf_bd = lambdify((w, b, u, d), expr=b_diff)(w=point[0], b=point[1], u=u_new, d=d_new)
	w_new, b_new = R(point[0] - h * ldf_wd), R(point[1] - h * ldf_bd)
	# в каждой итерации меняем значения координат
	point = (w_new, b_new, u_new, d_new)
	points += point,

print('w, b, u, d :', *point, sep='   ')
# print()
# print(*points, sep='\n')
