import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Определяем символьную переменную
x = sp.symbols('x')
# Запишем нашу функцию
function = x ** 3 - x

# Определим производную нашей функции
diff_function = sp.diff(function, x)

# Зададим начальное значение точки "a" и шаг
a0 = 1
h = 0.05

# Создадим переменную нашей производной для расчетов
lamb_diff_function = sp.lambdify(x, diff_function)


# Вычислим новые координаты точки "a" при помощи градиентного спуска и сохраним все значения в переменную "y"
y = [a0]
a = a0
while True:
	ldf = lamb_diff_function(a)
	a = a - ldf * h
	y.append(round(a, 3))
	if abs(ldf) < 0.008:
		break


# Генерируем данные для графика
x_value = np.linspace(start=0, stop=4, num=len(y))
y_value = [x ** 3 - x for x in x_value]
plt.plot(x_value, y_value)
plt.grid(True)

# Координаты градиентного спуска
x_grad = y
y_grad = [x ** 2 for x in y]
plt.scatter(x_grad, y_grad, color='red')

# Выводим график на экран
plt.show()
