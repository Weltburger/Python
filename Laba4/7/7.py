import sympy


def solve(*equalities):
    if len(equalities) == 1:
        return sympy.solve(equalities[0])
    return sympy.solve_poly_system(equalities)


x = sympy.Symbol("x", integer=True)
expr = x ** 2 * sympy.cos(1)
print('\nУравнение: ')
sympy.pprint(expr)
sympy.plot(expr)
print('\nПроизводная: ')
diff = sympy.diff(expr)
sympy.pprint(diff)
sympy.plot(diff)
print('\nИнтеграл: ')
integral = sympy.integrate(expr)
sympy.pprint(integral)
sympy.plot(integral)

y = sympy.Symbol("y")
eq1 = sympy.Equality(x ** 2 - x * y, 6)
eq2 = sympy.Equality(y ** 2 - x * y, -5)
eq3 = sympy.Equality(x ** 2 + sympy.cos(y), 0)

sympy.pprint(solve(eq1, eq2))
print('\n')
sympy.pprint(solve(eq3))
