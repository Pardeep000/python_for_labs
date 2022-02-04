import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x=sp.Symbol('x')

a=b=0#for definition
data=[]

met=input("Which method do you want to go with?\n1:Bisection method\n2:Regular-Falsi/False position method\n3:Newton-Raphson\n4:Secant Method\n")

if met=='1' or met=='2' or met=='3' or met=='4':
    exp=input("enter function in form of 'x': e.g. x**3-3*x-5 or 2*(x-3)-log(x) or cos(x)-x*exp(x) and ln(x)= log(x) / log (2.71828) where log(x)=log10(x)\n")

    func = parse_expr(exp)
    dfunc = sp.diff(exp)#For newton-raphson
    ##
    if met=='3':#For newton-raphson
        decision=input("Do you want to input:\n1:Interval\n2:Initial single value\n")
        if decision=='1':
            a=float(input("enter first number:\n"))
            b=float(input("enter second number:\n"))
            #For newton-raphson
            xo=(a+b)/2#choosing initial value
        elif decision=='2':
            xo=float(input("Enter initial value:\n"))
        else:
            print("Unwanted option\n")
    ##
    else:
        a=float(input("enter first number:\n"))
        b=float(input("enter second number:\n"))
        #For newton-raphson
        xo=(a+b)/2#choosing initial value
        decision='1'#checking'1' for keeping it true
    
    dec=input("choose one of them\n1:Stopping Criteria\n2:No. of iterations\n")
    if dec=='1':
        es=float(input("Enter stopping criteria:\n"))
    elif dec=='2':
        n=int(input("Enter no. of iterations:\n"))
    else:
        print("you chose for unwanted option...")

else:
    print("You chose for unwanted option...\n")
    exit()

    
def f(z):
    return sp.N(func.subs(x,z))
#for newton-raphson
def df(z):
    return sp.N(dfunc.subs(x,z))

error=100
i=1
pv=0


if f(a)*f(b)>0 and decision!='2': #and decision!='2' => By-passing condition for single value newton-raphson
    print("f(a) = ",f(a)," f(b) = ",f(b))
    print("wrong data has been entered...\n")

else:
    if met=='1':    
        if dec=='1':
            while error>es:
                c=(a+b)/2
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",i)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))

                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                i+=1
                pv=c
                print("root = ",format(c,"0.4f")," error = ",format(error,"0.4f"),"%")
            else:
                print("\nEnd...")
        elif dec=='2':
            for j in range(n):
                c=(a+b)/2
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",j+1)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))
                
                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                pv=c
                print("root = ",format(c,"0.4f")," error = ",format(error,"0.4f"),"%")
            else:
                print("\nEnd...")


    elif met=='2':
        if dec=='1':
            while error>es:
                c=(a*f(b)-b*f(a))/(f(b)-f(a))
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",i)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))

                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                i+=1
                pv=c
                print("root = ",format(c,"0.4f")," error = ",format(error,"0.4f"),"%")
            else:
                print("\nEnd...")
        elif dec=='2':
            for j in range(n):
                c=(a*f(b)-b*f(a))/(f(b)-f(a))
                cv=c
                error=(abs(cv-pv)/cv)*100
                
                print("\nIteration no. = ",j+1)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))
                
                if f(a)*f(c)<0:
                    b=c
                else:
                    a=c
                pv=c
                print("root = ",format(c,"0.4f")," error = ",format(error,"0.4f"),"%")
            else:
                print("\nEnd...")
    


    elif met=='3':
        if dec=='1':
            while error>es:
                c=xo-(f(xo)/df(xo))
                cv=c
                error=(abs(cv-pv)/cv)*100
                
                print("\nIteration no. = ",i)
                i+=1
                pv=c
                ##
                xo=c
                ##
                print("root = ",format(c,"0.4f")," error = ",format(error,"0.4f"),"%")
            else:
                print("\nEnd...")
        elif dec=='2':
            for j in range(n):
                c=xo-(f(xo)/df(xo))
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",j+1)

                pv=c
                xo=c

                print("root = ",format(c,"0.4f")," error = ",error,"%")
            else:
                print("\nEnd...")


    elif met=='4':
        if dec=='1':
            while error>es:
                c=(a*f(b)-b*f(a))/(f(b)-f(a))
                cv=c
                error=(abs(cv-pv)/cv)*100
                
                print("\nIteration no. = ",i)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))
                i+=1
                pv=c
                ##
                a=b
                b=c
                ##
                print("root = ",format(c,"0.6f")," error = ",format(error,'0.6f'),"%")
            else:
                print("\nEnd...")
        elif dec=='2':
            for j in range(n):
                c=(a*f(b)-b*f(a))/(f(b)-f(a))
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",j+1)
                print("a = ",a," b = ",b," c = ",c,"\nf(a) = ",f(a)," f(b) = ",f(b)," f(c) ",f(c))

                pv=c
                ##
                a=b
                b=c
                ##
                print("root = ",format(c,"0.6f")," error = ",format(error,'0.6f'),"%")
            else:
                print("\nEnd...")
