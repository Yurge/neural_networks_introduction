from sympy import symbols, diff, lambdify


# Сложная функция с несколькими аргументами
x1, x2, x3 = symbols('x1 x2 x3')
g1 = x2 + x3
g2 = x1 + x3
g3 = x1 + x2
f = g1 * g2 * g3

dx1 = diff(f, x1)
dx2 = diff(f, x2)
dx3 = diff(f, x3)

f_x1 = lambdify(args=(x1, x2, x3), expr=dx1)(x1=1, x2=2, x3=3)
f_x2 = lambdify(args=(x1, x2, x3), expr=dx2)(x1=1, x2=2, x3=3)
f_x3 = lambdify(args=(x1, x2, x3), expr=dx3)(x1=1, x2=2, x3=3)

print(f_x1, f_x2, f_x3, sep='\n')
