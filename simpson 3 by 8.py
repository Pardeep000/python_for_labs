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
while True:#condition for true working for simpson 1/3 rule
    n=int(input("enter no. of intervals:\n"))
    if n%3==0 and n>=3:
        break
    elif n<3:
        print("No. of intervals should not be less than '3'\nTry again:\n")
    elif n%3!=0 and n>=3:
        print("No. of intervals should be multiples of '3'\nTry again:\n")


h=(b-a)/n

n=n+1#for data points +1 as with no. of intervals

for i in range(n):
    value=i*h+a
    print(value)
    if value==a or value==b:
        sum+=f(value)
        print(f(value))
        #print("running in a and b")
        
    elif i%3==0 and i!=0:
        sum+=2*f(value)
        print(f(value))
        #print('got here in even')
        
    else:
        sum+=3*f(value)
        print(f(value))
        #print('got here in odd')
else:
    integral=(3*h/8)*sum
    print("\nIntegral = ",integral)


# 200*x**5-810*x**4+730*x**3-140*x**2+20*x+0.3

# 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
#0.2 and 0.8    
