import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

dec=input("What do you want to go with?\n1:Trapezoidal rule\n2:Simpson's 1/3 rule\n3:Simpson's 3/8 rule\n")
if dec=='1' or dec=='2' or dec=='3':
    exp=input("enter function in form of 'x':e.g 1/(1+x**2) or log(x) and loge(x) = 0.4343*log(x) for log10\n")
    func = parse_expr(exp)

    a=float(input("enter lower limit:\n"))
    b=float(input("enter upper limit:\n"))

    if dec=='1':
        n=int(input("enter no. of intervals:\n"))

    elif dec=='2':
        while True:#condition for true working for simpson 1/3 rule
            n=int(input("enter no. of intervals:\n"))
            if n%2==0 and n>=2:
                break
            elif n%2!=0 and n>2:
                print("No. of intervals should be even...\nEnter again")
            elif n<2:
                print("No. of intervals should not be less than '2'...\nEnter again")

    elif dec=='3':
        while True:#condition for true working for simpson 3/8 rule
            n=int(input("enter no. of intervals:\n"))
            if n%3==0 and n>=3:
                break
            elif n<3:
                print("No. of intervals should not be less than '3'\nTry again:\n")
            elif n%3!=0 and n>=3:
                print("No. of intervals should be multiples of '3'\nTry again:\n")
else:
    print("\nYou chose for unwanted option...\n")




def f(z):
    return sp.N(func.subs(x,z))

h=(b-a)/n
n=n+1#for data points +1 as with no. of intervals

sum=0

if dec=='1':
    for i in range(n):
        value=i*h+a
        if value==a or value==b:
            sum+=f(value)
        else:
            sum+=2*f(value)
    else:
        integral=(h/2)*sum
        print("\nIntegral = ",integral)

elif dec=='2':
    for i in range(n):
        value=i*h+a
        
        if value==a or value==b: #for end numbers
            sum+=f(value)
            
        elif i%2==0 and i!=0: #for even excluding '0'
            sum+=2*f(value)
            
        elif i%2==1:        #for odd
            sum+=4*f(value)
    else:
        integral=(h/3)*sum
        print("\nIntegral = ",integral)

elif dec=='3':
    for i in range(n):
        value=i*h+a
        
        if value==a or value==b:
            sum+=f(value)
            
        elif i%3==0 and i!=0:
            sum+=2*f(value)
            
        else:
            sum+=3*f(value)
    else:
        integral=(3*h/8)*sum
        print("\nIntegral = ",integral)
        
print("\nEnd...")
