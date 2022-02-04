import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

exp=input("enter function in form of 'x':\n")
f = parse_expr(exp)
df = sp.diff(exp)

a=float(input("enter first variable:\n"))
b=float(input("enter second variable:\n"))
xo=(a+b)/2#choosing initial value
dec=input("choose one of them\n1:Stopping Criteria\n2:No. of iterations\n")
if dec=='1':
    es=int(input("Enter stopping criteria:\n"))
elif dec=='2':
    n=int(input("Enter no. of iterations:\n"))
else:
    print("you chose for unwanted option...")


def func(z):
    return sp.N(f.subs(x,z))

def d_func(z):
    return sp.N(df.subs(x,z))


i=1
error=100
pv=0

if func(a)*func(b)>0:
        print("wrong data has been entered...\n")
else:
    if dec=='1':
        while error>es:
            c=xo-(func(xo)/d_func(xo))
            cv=c
            error=(abs(cv-pv)/cv)*100
            
            print("Iteration no. = ",i)
            i+=1
            pv=c
            ##
            xo=c
            ##
            print("root = ",c," f(c) = ",func(c))
        else:
            print("\nEnd...")
    elif dec=='2':
        for j in range(n):
            c=xo-(func(xo)/d_func(xo))
            cv=c
            error=(abs(cv-pv)/cv)*100

            print("Iteration no. = ",j+1)

            pv=c
            xo=c

            print("root = ",c," f(c) = ",func(c))
        else:
            print("\nEnd...")
