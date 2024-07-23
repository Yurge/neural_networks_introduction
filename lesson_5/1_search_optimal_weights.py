
from sympy import symbols, diff, lambdify


# ----------------- Поиск оптимальных значений весов при помощи градиентного спуска -----------------


# Определяем символьные переменные
w1, w0 = symbols('w1 w0')

# Запишем нашу функцию потерь
F_w = (w0 - 1) ** 2 + (w1 + w0 - 2) ** 2 + (2 * w1 + w0 - 3) ** 2

# Определим производные нашей функции
df_w0 = diff(F_w, w0)
df_w1 = diff(F_w, w1)
# print(df_w0, df_w1, sep='\n')

# Зададим первую точку и шаг
a0 = (0, 0)		# w0, w1
h = 0.1

# Находим все координаты градиентного спуска
point = a0
points = (a0,)
for _ in range(20):
	ldf_w0 = lambdify((w0, w1), expr=df_w0)(w0=point[0], w1=point[1])
	ldf_w1 = lambdify((w0, w1), expr=df_w1)(w0=point[0], w1=point[1])
	point = point[0] - h * ldf_w0, point[1] - h * ldf_w1
	points += point,
	if abs(ldf_w0) < 0.008 > abs(ldf_w1):
		break


w0_value, w1_value = point
print(w0_value, w1_value, sep='\n')
# мы знаем ответ на задачу (w0 и w1 должны быть равны 1) и за 20 итераций цикла наша программа почти идеально
# нашла оптимальные значения весов
