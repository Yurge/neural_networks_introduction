
from sympy import symbols, diff, lambdify
from random import sample


# ----------------- алгоритм стохастического градиентного спуска (СГС) по мини-батчам -----------------


# Определяем символьные переменные
w1, w0 = symbols('w1 w0')

# входные и целевые данные ТВ
x_val, y_val = [-1, 0, 1], [1, 0, -1]

# У нас простейшая НС. один аргумент на входе и по одному w1, w0
# Запишем функцию НС и Функцию Потерь
F = lambda x: x * w1 + w0
F_w = [(F(x) - y) ** 2 for x, y in zip(x_val, y_val)]

# Зададим первую точку и шаг
a0 = (0, 0)		# w0, w1
h = 0.1

# Находим все координаты градиентного спуска
# при СГС из Функции Потерь случайным образом отбирается 2 слагаемых в мини-батч...
point = a0
points = (a0,)
epoch = 5
butch_size = 2
for _ in range(epoch):										# кол-во эпох
	for _ in range(int(len(x_val) / butch_size)):			# одна эпоха
		func = sample(F_w, butch_size)						# отбираем 2 случайных элемента из Ф-ии Потерь
		mini_butch = func[0] + func[1]						# составляем мини-батч из butch_size слагаемых
		df_w1 = diff(mini_butch, w1)				# находим производные
		df_w0 = diff(mini_butch, w0)
		ldf_w1 = lambdify((w0, w1), expr=df_w1)(w0=point[0], w1=point[1])
		ldf_w0 = lambdify((w0, w1), expr=df_w0)(w0=point[0], w1=point[1])
		point = point[0] - h * ldf_w0, point[1] - h * ldf_w1
		points += point,
		if abs(ldf_w0) < 0.008 > abs(ldf_w1):
			break


# print(*points, sep='\n')
w0_optim, w1_optim = point							# Сохраним оптимальные веса для предсказания новых данных
print(w0_optim, w1_optim)
