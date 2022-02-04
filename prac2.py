import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr

def deg(z):
    return z*(sp.pi/180)

x=sp.Symbol('x')
f=input("enter expression:\n")
df = sp.diff(f)

exp = parse_expr(f)
r1=exp.subs(x,5)
print(sp.N(r1))

r2=df.subs(x,5)
print(sp.N(r2))




##func=input("enter sth:\n")
##def funcc(x):
##    return eval(func)
##r1=sp.N(funcc(2))
##print("\nr1 = ",r1)
##
###x=sp.Symbol('x')
##d_func=sp.diff(func)
###r2=d_func.subs(x,2)
###print("\nr2 = ",r2)
###print(d_func)


##func=input("enter expression:\n")
##x=sp.Symbol('x')
##exp=sp.cos(x)
##r=exp.subs(x,deg(180))
##print(sp.N(r))
