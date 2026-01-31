import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sqrt, lambdify

x, y, r = symbols('x, y, r', real=True)

eq1 = Eq(2*x**2 + 3*y**2, r)
eq2 = Eq(y - 2*x, 1)

sol = solve([eq1, eq2], [x, y], dict=True)

r_val = 10

points = [(float(s[x].subs(r, r_val)), 
           float(s[y].subs(r, r_val))) for s in sol]

y_line = lambdify(x, 2*x + 1, 'numpy')

y_ellipse = lambdify(x, sqrt((r_val - 2*x**2)/3), 'numpy')

x_vals = np.linspace(-np.sqrt(5), np.sqrt(5), 400)

plt.plot(x_vals, y_line(x_vals), label='y=2x+1')

plt.plot(x_vals, y_ellipse(x_vals), label='2x^2 + 3y^2 = 10')
plt.plot(x_vals, -y_ellipse(x_vals))

for px, py in points:
    plt.plot(float(px), float(py),
             marker='*', markersize='10',
             markeredgecolor='black', markerfacecolor='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse and Line')
plt.grid(True)
plt.legend()
plt.savefig('Problem2.pdf')
plt.show()


