# ------------------------------------ ИНИЦИАЛИЗАЦИЯ ВЕСОВ ------------------------------------


# Начальные значения весов-связей (w1) между слоями задаётся случайными числами из диапазона
# [-1/n, 1/n], где n - количество нейронов в каждом из двух полносвязных слоёв.

# Если в соседних слоях разное количество нейронов, тогда n находим как среднее арифметическое,
# n = (n1 + n2) / 2


# ------------------------------------ НОРМАЛИЗАЦИЯ  ДАННЫХ ------------------------------------

import pandas as pd


# В разных колонках могут быть совершенно разные данные с разным размахом,
# допустим в колонке Вес могут быть данные от 10 до 160 с шагом = 1,
# а в колонке Пол мы видим данные либо 0, либо 1.
# Данные нужно нормализовать, т.е. привести к одному виду.
# Это делается ПЕРЕД обучением НС.
# Новые данные, поступившие для предсказания, тоже потребуется нормализовать.

data = pd.DataFrame({
	'Пациент': ['A1', 'A2', 'A3', 'A4'],
	'Вес': [50, 60, 80, 100],
	'Пол': [0, 1, 1, 0]
					})

print(data, '\n')


def normalise(column):
	a = data[column].min()
	b = data[column].max()
	norm = pd.Series(data[column] - a) / (b - a)
	return norm


data['weight_n'] = normalise('Вес')
data['gender_n'] = normalise('Пол')
print(data, '\n')
