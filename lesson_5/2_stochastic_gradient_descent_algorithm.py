
from sympy import symbols, diff, lambdify
from random import choice


# ----------------- алгоритм стохастического градиентного спуска (СГС) -----------------


# Определяем символьные переменные
w1, w0 = symbols('w1 w0')

# входные и целевые данные ТВ
x_val, y_val = [0, 1, 2], [1, 2, 3]

# У нас простейшая НС. один аргумент на входе и по одному w1, w0
# Запишем функцию НС и функцию потерь
F = lambda x: x * w1 + w0
F_w = [(F(x) - y) ** 2 for x, y in zip(x_val, y_val)]

# Зададим первую точку и шаг
a0 = (0, 0)		# w0, w1
h = 0.1

# Находим все координаты градиентного спуска
# при СГС из Функции Потерь случайным образом отбирается одно слагаемое...
point = a0
points = (a0,)
epoch = 5
for _ in range(epoch):								# Кол-во эпох
	for _ in range(len(x_val)):						# одна эпоха - размер ТВ
		func = choice(F_w)							# Отбираем одно слагаемое
		df_w1 = diff(func, w1)				# находим производные
		df_w0 = diff(func, w0)
		ldf_w1 = lambdify((w0, w1), expr=df_w1)(w0=point[0], w1=point[1])
		ldf_w0 = lambdify((w0, w1), expr=df_w0)(w0=point[0], w1=point[1])
		point = point[0] - h * ldf_w0, point[1] - h * ldf_w1
		points += point,
		if abs(ldf_w0) < 0.008 > abs(ldf_w1):
			break

print(*points, sep='\n')
w0_optim, w1_optim = point							# Сохраним оптимальные веса для предсказания новых данных
print(w0_optim, w1_optim)
