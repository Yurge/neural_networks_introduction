#  Искусственный нейрон с двумя входными значениями
# Задаём входные значения, веса, смещение
x = (1, 2)
w = (2, 1)
w0 = 4


def neural(data_in, weights, offset):
	s = []
	for ind in range(len(data_in)):
		s.append(data_in[ind] * weights[ind])
	result_s = sum(s) + offset
	relu = max(result_s, 0)
	return relu


data_out = neural(x, w, w0)
print(data_out)




# Поиск w1 и w0 если   4 * w1 + w0 = 1   и   2 * w1 + w0 = 3
from sympy import symbols, solve

w1, w0 = symbols('w1 w0')
func = lambda x: x * w1 + w0

f1 = func(1) - 0.5
f2 = func(2) - 0.5

vals = solve((f1, f2), (w1, w0))
print(vals)

# Теперь, имея значения w1 и w0, посчитаем func при x=0
X = 0
print(func(X).subs(vals))



# Вычислить Fnn, если входной слой из 1 элемента, далее 1 внутренний слой из 2 элементов,
# затем выходной слой из 1 элемента
x = 2
w1_11 = 1
w1_12 = 2
w0_11 = 1
w0_12 = -5
w1_21 = -2
w1_22 = 4
w0_2 = 10
f = lambda x: max(0, x)

Fnn = f(f(x * w1_11 + w0_11) * w1_21 + f(x * w1_12 + w0_12) * w1_22 + w0_2)
print(Fnn)