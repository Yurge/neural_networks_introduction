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
