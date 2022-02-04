import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

exp=input("enter function in form of 'x':\n")
f = parse_expr(exp)
df = sp.diff(exp)

a=float(input("enter first variable:\n"))
b=float(input("enter second variable:\n"))

dec=input("choose one of them\n1:Stopping Criteria\n2:No. of iterations\n")
if dec=='1':
    es=float(input("Enter stopping criteria:\n"))
elif dec=='2':
    n=int(input("Enter no. of iterations:\n"))
else:
    print("you chose for unwanted option...")


def func(z):
    return sp.N(f.subs(x,z))

i=1
error=100
pv=0

if func(a)*func(b)>0:
        print("wrong data has been entered...\n")
else:
    if dec=='1':
        while error>es:
            c=(a*func(b)-b*func(a))/(func(b)-func(a))
            cv=c
            error=(abs(cv-pv)/cv)*100
            
            print("\nIteration no. = ",i)
            print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",func(a)," f(b) = ",func(b)," f(c) ",func(c))
            i+=1
            pv=c
            ##
            a=b
            b=c
            ##
            print("root = ",c," error = ",error)
        else:
            print("\nEnd...")
    elif dec=='2':
        for j in range(n):
            c=(a*func(b)-b*func(a))/(func(b)-func(a))
            cv=c
            error=(abs(cv-pv)/cv)*100

            print("\nIteration no. = ",j+1)
            print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",func(a)," f(b) = ",func(b)," f(c) ",func(c))

            pv=c
            ##
            a=b
            b=c
            ##
            print("root = ",c," error = ",error)
        else:
            print("\nEnd...")




'''
x**3-6*x**2+11*x-6.1  =>  (2.5,3.5,0.1)

'''
