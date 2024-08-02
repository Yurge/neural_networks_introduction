# --------------------------------  ГС для задачи мультиклассовой классификации  -----------------------------

# У нас 2 объекта и в каждом только одна переменная "х", на выходе получаем 3 класса (A, B, C)

from sympy import symbols, diff, lambdify, ln
from math import e


x_val, y_val = [-1, 0, 1], [0, 1, 2]

# Определяем символьные переменные
w1, w2, w3, w4, w5, w6 = symbols('w1, w2, w3, w4, w5, w6', real=True)

# Запишем выходные значения A и B для каждого объекта из ТВ
A1, B1, C1 = -w1 + w4, -w2 + w5, -w3 + w6
A2, B2, C2 = w4, w5, w6
A3, B3, C3 = w1 + w4, w2 + w5, w3 + w6


# Запишем функции Softmax (определим вероятности выходных значений)
pr_y0 = lambda A, B, C: e ** A / (e ** A + e ** B + e ** C)		# Если целевой показатель y = 0
pr_y1 = lambda A, B, C: e ** B / (e ** A + e ** B + e ** C)		# Если целевой показатель y = 1
pr_y2 = lambda A, B, C: e ** C / (e ** A + e ** B + e ** C)		# Если целевой показатель y = 2

# Запишем функцию потерь для всех 2 объектов
F_w = -ln(pr_y0(A1, B1, C1)) - ln(pr_y1(A2, B2, C2)) - ln(pr_y2(A3, B3, C3))

# Вычислим производные для всех весов
df_w1 = diff(F_w, w1)
df_w2 = diff(F_w, w2)
df_w3 = diff(F_w, w3)
df_w4 = diff(F_w, w4)
df_w5 = diff(F_w, w5)
df_w6 = diff(F_w, w6)

# print(df_w1, df_w2, df_w3, df_w4, sep='\n')

# Зададим начальные координаты и величину шага
a0 = 0, 0, 0, 0, 0, 0		# w1, w2, w3, w4, w5, w6
h = 0.04

# ГС:
p = a0
points = a0,
for num in range(1, 2):
	ldf_w1 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w1)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	ldf_w2 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w2)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	ldf_w3 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w3)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	ldf_w4 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w4)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	ldf_w5 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w5)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	ldf_w6 = lambdify((w1, w2, w3, w4, w5, w6), expr=df_w6)(w1=p[0], w2=p[1], w3=p[2], w4=p[3], w5=p[4], w6=p[5])
	p = (p[0] - ldf_w1 * h, p[1] - ldf_w2 * h, p[2] - ldf_w3 * h,
		 p[3] - ldf_w4 * h, p[4] - ldf_w5 * h, p[5] - ldf_w6 * h)
	points += p,
	# print(f'шаг а{num}. \n  w1,  w2,  w3,  w4  : \n{p}')
	# print()

print(f'  w1,  w2,  w3,  w4, w5, w6  : \n{p}')
# print(lambdify(w, df)(-2), sep='\n')
