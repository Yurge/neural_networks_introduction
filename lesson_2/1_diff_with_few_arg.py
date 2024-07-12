import sympy as sp


args = 'x1 x2 x3'
# Определяем символьные переменные
x1, x2, x3 = sp.symbols(args)

# Запишем нашу функцию
function = sp.ln(x1*x2 + x1*x3)

# Определим все производные нашей функции
df = {x: sp.diff(function, x) for x in args.split()}
print(df)

# Рассчитаем, чему будет равно значение производной первого аргумента (х1) в точке (4, 2, 1)
print(df['x1'].subs({x1: 4, x2: 2, x3: 1}))
