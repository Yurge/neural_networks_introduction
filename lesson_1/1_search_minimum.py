import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Создание символьной переменной x
x = sp.symbols('x')
# Указываем вид нужной функции
func = x * (x ** 2 - 9)
print(f'функция = {func}')

# Находим производную (дифференциал) по нашей функции
func_diff = sp.diff(func, x)
print(f'производная функции = {func_diff}')

# Находим все точки ЛОКАЛЬНЫХ экстремумов и округляем до требуемой точности
all_solutions = [round(i, 2) for i in sp.solve(func_diff, x)]
# Выводим минимум
print('Значение в минимуме (локальный минимум по оси Х):', min(all_solutions))


# Генерируем данные для графика
x_value = np.linspace(-3, 3, 10)
y_value = [x * (x ** 2 - 9) for x in x_value]
plt.plot(x_value, y_value)
plt.grid(True)

plt.show()
