# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:15:10 2017

@author: andrea
"""

from sympy import symbols, Function, Eq, dsolve, sin, init_printing, pretty
init_printing()

x, C1, C2 = symbols('x C1 C2')
f, g, h, F = symbols('f g h F', cls=Function)
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
print(pretty(diffeq))

#from sympy import classify_ode
#print(classify_ode(diffeq,f(x)))

#sol=dsolve(diffeq, f(x), ics={f(0):1,f(x).diff(x).subs(x, 0):0})
sol=dsolve(diffeq, f(x))
#print(sol)


g = sol.rhs
#print("f(x) = ", g)
h = g.diff(x)
#print("f'(x) = ", h)

IC1 = 1
IC2 = 0
expr1 = g.subs(x,0)-IC1
#print(expr1)
expr2 = h.subs(x,0)-IC2
#print(expr2)

from sympy import linsolve
wIC = linsolve([expr1, expr2], C1, C2)
#print("initial condition solution:", wIC)
#print("C2 =", wIC.args[0][1])
f0, f10 = next(iter(wIC))
#print("C1 =", f0, "\tC2 =", f10 )

F = sol.rhs.subs(C1,f0).subs(C2,f10)
print(pretty(F))

from sympy.plotting import plot
plot(F,(x,0,1))