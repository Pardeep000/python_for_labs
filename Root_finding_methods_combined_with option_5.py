import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt

x=sp.Symbol('x')

a=b=0 #for definition
a_original=b_original=0 #for definition


data=[]
c_error=[]
c_data=[]

met=input("Which method do you want to go with?\n1:Bisection method\n2:Regular-Falsi/False position method\n3:Newton-Raphson\n4:Secant Method\n5:Combined method\n")

if met=='1' or met=='2' or met=='3' or met=='4' or met=='5':
    exp=input("enter function in form of 'x': e.g. x**3-3*x-5 or cos(x)-x*exp(x)\n")

    func = parse_expr(exp)
    dfunc = sp.diff(exp)#For newton-raphson
    ##
    if met=='3':#For newton-raphson
        decision=input("Do you want to input:\n1:Interval\n2:Initial single value\n")
        if decision=='1':
            a_original=float(input("enter first number:\n"))
            b_original=float(input("enter second number:\n"))
            #
            a=a_original
            b=b_original
            #For newton-raphson
            xo=(a+b)/2#choosing initial value
        elif decision=='2':
            xo=float(input("Enter initial value:\n"))
        else:
            print("Unwanted option\n")
    ##
    else:
        a_original=float(input("enter first number:\n"))
        b_original=float(input("enter second number:\n"))
        #
        a=a_original
        b=b_original
        #For newton-raphson
        xo=(a+b)/2#choosing initial value
        decision='2'#checking
    
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






##combined all root finding methods

    elif met=='5':  
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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original

                print("\nBisection method\n")

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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)

                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original              

                print("\nBisection method\n")


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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original
                
                print("\nRoot finding method\n")
                
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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original
                
                print("\nRoot finding method\n")

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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original
                
                print("\nNewton Raphson method\n")
        elif dec=='2':
            for j in range(n):
                c=xo-(f(xo)/df(xo))
                cv=c
                error=(abs(cv-pv)/cv)*100

                print("\nIteration no. = ",j+1)

                pv=c
                xo=c

                print("root = ",format(c,"0.4f")," error = ",error,"%")
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original
                
                print("\nNewton Raphson method\n")


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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original
                
                print("\nSecant method\n")
                
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
                ##for combined method
                data.append(c)
                c_error.append(error)
            else:
                c_data.append(data)
                c_data.append(c_error)
                
                ##cleaing the lists
                error=100
                i=1
                pv=0
                data=[]
                c_error=[]
                a=a_original
                b=b_original

                print("\nSecant method\n")

if met=='5':
    x_values=[]
    data_acc=[]
        
    max_len1=max([len(c_data[0]),len(c_data[2]),len(c_data[4]),len(c_data[6])])
    max_len2=max([len(c_data[1]),len(c_data[3]),len(c_data[5]),len(c_data[7])])
##    print("max-len1 = ",max_len1)
##    print("max-len2 = ",max_len2)
##    print("len(c_data[i]) = ",len(c_data))
    
    if dec=='1': #For stopping criteria case
        for i in range(len(c_data)):
            for j in range(len(c_data[i])):
                data_acc.append(j+1)
            else:
                #print("data_acc = ",data_acc)
                x_values.append(data_acc)
                data_acc=[]

    else: #For no. of iterations case
        for i in range(len(c_data)+1):
            for j in range(max_len2):
                data_acc.append(j+1)
            else:
                #print("data_acc = ",data_acc)
                x_values.append(data_acc)
                data_acc=[]
##    for i in range(len(c_data)):
##        print("x_values2[",i,"] = ",x_values2[i])
    plt.subplot(1,2,1)
    plt.plot(x_values[0],c_data[0],'b--',label="Bisection",marker='o')
    plt.plot(x_values[2],c_data[2],'g--',label="Regular Falsi",marker='o')
    plt.plot(x_values[4],c_data[4],'r--',label="Newton-Raphson",marker='o')
    plt.plot(x_values[6],c_data[6],'y--',label="Secant method",marker='o')
    plt.legend(loc='upper center')
    plt.title("Root finding methods solutions comparision\n")
    #plt.show()

    plt.subplot(1,2,2)
    plt.plot(x_values[1],c_data[1],'b--',label="Bisection",marker='o')
    plt.plot(x_values[3],c_data[3],'g--',label="Regular Falsi",marker='o')
    plt.plot(x_values[5],c_data[5],'r--',label="Newton-Raphson",marker='o')
    plt.plot(x_values[7],c_data[7],'y--',label="Secant method",marker='o')
    plt.legend(loc='upper center')
    plt.title("Root finding methods Error comparision\n")
    plt.show()
