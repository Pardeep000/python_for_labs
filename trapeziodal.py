import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

exp=input("enter function in form of 'x':\n")
func = parse_expr(exp)

sum=0

def f(z):
    return sp.N(func.subs(x,z))

a=float(input("enter lower limit:\n"))
b=float(input("enter upper limit:\n"))
n=int(input("enter no. of intervals:\n"))

h=(b-a)/n

n=n+1#for data points +1 as with no. of intervals

for i in range(n):
    value=i*h+a
    if value==a or value==b:
        sum+=f(value)
    else:
        sum+=2*f(value)
else:
    integral=(h/2)*sum
    print("\nIntegral = ",integral)


# 200*x**5-810*x**4+730*x**3-140*x**2+20*x+0.3
#0.2 and 0.8    
