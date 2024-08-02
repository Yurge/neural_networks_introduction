# --------------------------------  ГС для задачи классификации  -----------------------------


from sympy import symbols, diff, lambdify, ln
from math import e

# У нас 3 объекта и в каждом только одна переменная "х"
x_val, y_val = [-1, 0, 1], [0, 1, 0]

# Определяем символьные переменные
w1, w2, w3, w4 = symbols('w1, w2, w3, w4', real=True)

# Запишем выходные значения A и B для каждого объекта из ТВ
A1, B1 = -w1 + w3, -w2 + w4
A2, B2 = w3, w4
A3, B3 = w1 + w3, w2 + w4


# Запишем функции Softmax
pr_y0 = lambda A, B: e ** A / (e ** A + e ** B)		# Если целевой показатель y = 0
pr_y1 = lambda A, B: e ** B / (e ** A + e ** B)		# Если целевой показатель y = 1

# Запишем функцию потерь для всех 3 объектов
F_w = -ln(pr_y0(A1, B1)) - ln(pr_y1(A2, B2)) - ln(pr_y0(A3, B3))

# Вычислим производные для всех весов
df_w1 = diff(F_w, w1)
df_w2 = diff(F_w, w2)
df_w3 = diff(F_w, w3)
df_w4 = diff(F_w, w4)

# print(df_w1, df_w2, df_w3, df_w4, sep='\n')

# Зададим начальные координаты и величину шага
a0 = 0, 0, 0, 0		# w1, w2, w3, w4
h = 0.1

# ГС:
point = a0
points = a0,
for num in range(1, 20):
	ldf_w1 = lambdify((w1, w2, w3, w4), df_w1)(w1=point[0], w2=point[1], w3=point[2], w4=point[3])
	ldf_w2 = lambdify((w1, w2, w3, w4), df_w2)(w1=point[0], w2=point[1], w3=point[2], w4=point[3])
	ldf_w3 = lambdify((w1, w2, w3, w4), df_w3)(w1=point[0], w2=point[1], w3=point[2], w4=point[3])
	ldf_w4 = lambdify((w1, w2, w3, w4), df_w4)(w1=point[0], w2=point[1], w3=point[2], w4=point[3])
	point = (point[0] - ldf_w1 * h, point[1] - ldf_w2 * h,
			 point[2] - ldf_w3 * h, point[3] - ldf_w4 * h)
	points += point,
	# print(f'шаг а{num}. \n  w1,  w2,  w3,  w4  : \n{point}')
	# print()

print(f'  w1,  w2,  w3,  w4  : \n{point}')
# print(lambdify(w, df)(-2), sep='\n')
