from sympy import symbols, diff, lambdify


# ------------------------------------------- transfer learning -------------------------------------------

# Сейчас существуют уже готовые натренированные СНС общего назначения. Можно взять такую НС и дообучить её на ваших
# данных. Технология transfer learning подразумевает два способа дообучения:




# ------------------------------------------------ 1 способ -----------------------------------------------
# Веса первого слоя замораживают, чтобы они не менялись. Почему? Потому что в первых слоях установлены самые общие
# и базовые закономерности, которые можно не менять.

# Определяем символьные переменные
w1, b1, w2, b2 = symbols('w1, b1, w2, b2')

# входные и целевые данные ТВ
x_val, y_val = [-2, 2], [4, 4]

# Запишем функцию НС и функцию потерь
Fnn = lambda x: (w1 * x + b1) * w2 + b2
F_w = sum((Fnn(x) - y) ** 2 for x, y in zip(x_val, y_val))

# находим производные
df_w1 = diff(F_w, w1)
df_b1 = diff(F_w, b1)
df_w2 = diff(F_w, w2)
df_b2 = diff(F_w, b2)


# оптимальные веса нам уже известны, выставляем их как начальные
a0 = (1, 1, 1, -1)		# w1, b1, w2, b2
h = 0.1


# В ходе итераций меняются только веса второго слоя (w2, b2). Первые веса "замораживаем" и не меняем
point = a0
points = (a0,)
for _ in range(1):
	ldf_w2 = lambdify((w1, b1, w2, b2), expr=df_w2)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	ldf_b2 = lambdify((w1, b1, w2, b2), expr=df_b2)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	point = 1, 1, point[2] - h * ldf_w2, point[3] - h * ldf_b2
	points += point,

print(points)




# ------------------------------------------------ 2 способ -----------------------------------------------
# Весам начальных слоёв будем давать меньший шаг, чтобы они менялись не очень сильно

# Определяем символьные переменные
w1, b1, w2, b2 = symbols('w1, b1, w2, b2')

# входные и целевые данные ТВ
x_val, y_val = [-2, 2], [4, 4]


# Запишем функцию НС и функцию потерь
Fnn = lambda x: (w1 * x + b1) * w2 + b2
F_w = sum((Fnn(x) - y) ** 2 for x, y in zip(x_val, y_val))

# находим производные
df_w1 = diff(F_w, w1)
df_b1 = diff(F_w, b1)
df_w2 = diff(F_w, w2)
df_b2 = diff(F_w, b2)

# оптимальные веса нам уже известны, выставляем их как начальные
a0 = (1, 1, 1, -1)		# w1, b1, w2, b2
h1 = 0.05				# на первый слой
h2 = 0.1				# на второй слой

# на новых данных вычисляем новые оптимальные веса при помощи ГС
point = a0
points = (a0,)
for _ in range(1):
	ldf_w1 = lambdify((w1, b1, w2, b2), expr=df_w1)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	ldf_b1 = lambdify((w1, b1, w2, b2), expr=df_b1)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	ldf_w2 = lambdify((w1, b1, w2, b2), expr=df_w2)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	ldf_b2 = lambdify((w1, b1, w2, b2), expr=df_b2)(w1=point[0], b1=point[1], w2=point[2], b2=point[3])
	point = point[0] - h1 * ldf_w1, point[1] - h1 * ldf_b1, point[2] - h2 * ldf_w2, point[3] - h2 * ldf_b2
	points += point,

# print(point)
# print(points)