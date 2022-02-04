import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

met=input("What method do you want to go with?\n1:Bisection method\n2:Regular Falsi method\n")

if met=='1' or met=='2':
    exp=input("enter function in form of 'x':\n")

    func = parse_expr(exp)
    
    a=float(input("enter first variable:\n"))
    b=float(input("enter second variable:\n"))
    
    dec=input("choose one of them\n1:Stopping Criteria\n2:No. of iterations\n")
    if dec=='1':
        es=float(input("Enter stopping criteria:\n"))
    elif dec=='2':
        n=int(input("Enter no. of iterations:\n"))
    else:
        print("you chose for unwanted option...")

else:
    print("You chose for unwanted option...\n")

    
def f(z):
    return sp.N(func.subs(x,z))


error=100
i=1
pv=0

if met=='1':
    if f(a)*f(b)>0:
        print("f(a) = ",f(a)," f(b) = ",f(b))
        print("wrong data has been entered...\n")
    else:
        if dec=='1':
            while error>es:
                c=(a+b)/2
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b))

                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                print("Iteration no. = ",i)
                i+=1
                pv=c
                print(" f(c) = ",f(c))
            else:
                print("\nEnd...")
        elif dec=='2':
            for j in range(n):
                c=(a+b)/2

                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b))
                
                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                print("Iteration no. = ",j+1)
                pv=c
                print(" f(c) = ",f(c))
            else:
                print("\nEnd...")
elif met=='2':
        if f(a)*f(b)>0:
            print("wrong data has been entered...\n")
        else:
            if dec=='1':
                while error>es:
                    c=(a*f(b)-b*f(a))/(f(b)-f(a))
                    cv=c
                    error=(abs(cv-pv)/cv)*100

                    print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b))

                    if f(a)*f(c)<0:
                        b=c
                    else:
                        a=c
                    print("Iteration no. = ",i)
                    i+=1
                    pv=c
                    print(" f(c) = ",f(c))
                else:
                    print("\nEnd...")
            elif dec=='2':
                for j in range(n):
                    c=(a*f(b)-b*f(a))/(f(b)-f(a))

                    print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b))
                    
                    if f(a)*f(c)<0:
                        b=c
                    else:
                        a=c
                    print("Iteration no. = ",j+1)
                    pv=c
                    print(" f(c) = ",f(c))
                else:
                    print("\nEnd...")
    
