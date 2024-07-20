# ------------------------------ Искусственный нейрон с двумя входными значениями -------------------------------


# Задаём входные значения, веса, смещение
x = (1, 2)
w = (2, 1)
w0 = 4


def neural(data_in, weights, offset):
	s = []
	for ind in range(len(data_in)):
		s.append(data_in[ind] * weights[ind])
	result = sum(s) + offset
	return 0 if result <= 0 else result


data_out = neural(x, w, w0)

print(data_out)




# ----------------   Поиск w1 и w0 если   4 * w1 + w0 = 1   и   2 * w1 + w0 = 3  ------------
from sympy import symbols, solve

w1, w0 = symbols('w1 w0')
func = lambda x: x * w1 + w0

f1 = func(4) - 1
f2 = func(2) - 3

vals = solve((f1, f2), (w1, w0))
print(vals)

X = 0
# print(func(X).subs(vals))
