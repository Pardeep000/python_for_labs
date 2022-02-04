from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sympy as sp


exp=input("f(x,y) = ")
a=float(input("initial x-value: "))
b=float(input("final x-value: "))
yo=float(input("initial y-value: "))
h=float(input("step size: "))
n=int((b-a)/h)



val=a
yo_h=yo

data=[]
c_data=[]

error_val=[]

x_val=[] #for graph and for true values

## For true values/ analytical solutions
###########################
def derivative(y,x):
    return eval(exp)

def solve(x,yo):
    return odeint(derivative,yo,x)

for i in range(int(n)+1):
    x_val.append(val)
    val+=h
else:
    true_val=solve(x_val,yo)
    val=a
    true_val = true_val.ravel()
    print(true_val)
    print(len(true_val))
    c_data.append(true_val)
###########################



def f(x,y):
    return eval(exp)

a2,a1,p1,q11=sp.symbols("a1 a2 p1 q11")

e1=sp.Eq(a1+a2,1)
e2=sp.Eq(a2*p1,1/2)
e3=sp.Eq(a2*q11,1/2)



dec=input("Which one?\n1:Heun\n2:Mid-point\n3:Raltson\n4:For all\n")
if dec=='1':
    val_a2=1/2 #for Heun Method (val = a2 = 1/2)
    ##
    r1 = e1.subs(a2,val_a2)
    r2 = e2.subs(a2,val_a2)
    r3 = e3.subs(a2,val_a2)
    r = sp.solve((r1,r2,r3),(a1,p1,q11))
    
    for i in range(int(n)+1):
        k1=f(float(val),float(yo_h))
        k2=f(float(val+r[p1]*h) , float(yo_h+r[q11]*k1*h))
        thita = r[a1]*k1 + val_a2*k2
        ##
        y_new = yo_h + thita*h
        data.append(y_new)

        yo_h=y_new
        val+=h
        
    else:
        data.insert(0,yo)
        data.pop()

        ##
        for i in range(int(n)+1):
            #error calculation
            error=(abs(data[i]-true_val[i])/true_val[i])*100
            error_val.append(error)
            #error
        else:
            c_data.append(data)
            c_data.append(error_val)

            ##Displaying data numerically:
            panda_data=pd.DataFrame(c_data)
            panda_data=panda_data.T
            panda_data.columns=["y_true","y_Heun" , "Heun_error"]
            panda_data.index=x_val
            print(panda_data)

            ##Displaying data graphically:\n
            plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
            plt.plot(x_val,data,'g--',label="Heun_values",marker='o')
            plt.legend(loc='upper center')
            plt.title("Approx. and Exact solutions of ODE")
            plt.show()
            
elif dec=='2':
    val_a2=1 #for Mid-point method
    ##
    r1 = e1.subs(a2,val_a2)
    r2 = e2.subs(a2,val_a2)
    r3 = e3.subs(a2,val_a2)
    r = sp.solve((r1,r2,r3),(a1,p1,q11))

    for i in range(int(n)+1):
        k1=f(float(val),float(yo_h))
        k2=f(float(val+r[p1]*h) , float(yo_h+r[q11]*k1*h))
        thita = r[a1]*k1 + val_a2*k2
        ##
        y_new = yo_h + thita*h
        data.append(y_new)

        yo_h=y_new
        val+=h
        
    else:
        data.insert(0,yo)
        data.pop()
        ##
        for i in range(int(n)+1):
            #error
            error=(abs(data[i]-true_val[i])/true_val[i])*100
            error_val.append(error)
            #error
        else:
            c_data.append(data)
            c_data.append(error_val)

            ##Displaying data numerically:
            panda_data=pd.DataFrame(c_data)
            panda_data=panda_data.T
            panda_data.columns=["y_true","y_Mid-points" , "Mid-points_error"]
            panda_data.index=x_val
            print(panda_data)

            ##Displaying data graphically:\n
            plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
            plt.plot(x_val,data,'g--',label="Mid-points_values",marker='o')
            plt.legend(loc='upper center')
            plt.title("Approx. and Exact solutions of ODE")
            plt.show()
            
elif dec=='3':
    val_a2=2/3 #for Raltson's method
    ##
    r1 = e1.subs(a2,val_a2)
    r2 = e2.subs(a2,val_a2)
    r3 = e3.subs(a2,val_a2)
    r = sp.solve((r1,r2,r3),(a1,p1,q11))

    for i in range(int(n)+1):
        k1=f(float(val),float(yo_h))
        k2=f(float(val+r[p1]*h) , float(yo_h+r[q11]*k1*h))
        thita = r[a1]*k1 + val_a2*k2
        ##
        y_new = yo_h + thita*h
        data.append(y_new)

        yo_h=y_new
        val+=h
        
    else:
        data.insert(0,yo)
        data.pop()
        #
        for i in range(int(n)+1):
            #error
            error=(abs(data[i]-true_val[i])/true_val[i])*100
            error_val.append(error)
            #error
        else:
            c_data.append(data)
            c_data.append(error_val)

            ##Displaying data numerically:
            panda_data=pd.DataFrame(c_data)
            panda_data=panda_data.T
            panda_data.columns=["y_true","y_Raltson" , "Raltson_error"]
            panda_data.index=x_val
            print(panda_data)

            ##Displaying data graphically:\n
            plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
            plt.plot(x_val,data,'g--',label="Raltson_values",marker='o')
            plt.legend(loc='upper center')
            plt.title("Approx. and Exact solutions of ODE")
            plt.show()
elif dec=='4':
    a2_list=[1/2,1,2/3]
    for i in range(3):
        val_a2=a2_list[i]
        ##
        r1 = e1.subs(a2,val_a2)
        r2 = e2.subs(a2,val_a2)
        r3 = e3.subs(a2,val_a2)
        r = sp.solve((r1,r2,r3),(a1,p1,q11))
        #print("Data = ",i+1)
        for i in range(int(n)+1):
            k1=f(float(val),float(yo_h))
            k2=f(float(val+r[p1]*h) , float(yo_h+r[q11]*k1*h))
            thita = r[a1]*k1 + val_a2*k2
            ##
            y_new = yo_h + thita*h
            data.append(y_new)
            
            yo_h=y_new
            val+=h
            
            ##
            
        else:
            data.insert(0,yo)
            data.pop()
            #print(data)
            for i in range(int(n)+1):
                #error
                error=(abs(data[i]-true_val[i])/true_val[i])*100
                error_val.append(error)
                #error
            
            c_data.append(data)
            data=[]
            c_data.append(error_val)
            error_val=[]
            
            yo_h=yo
            val=a
            
    else:
        ##Displaying data numerically:\n
        pd.set_option('display.max_columns',7)
        panda_data=pd.DataFrame(c_data)
        panda_data=panda_data.T
        panda_data.columns=["y_true","y_heun" , "Heun_error" , "y_mid-point" , "Mid_error" , "y_raltson","Raltson_error"]
        print(panda_data)

        ##Displaying data graphically:\n
        plt.subplot(1,2,1)
        plt.plot(x_val,c_data[0],'b--',label="True_values",marker='o')
        plt.plot(x_val,c_data[1],'g--',label="Heun_values",marker='o')
        plt.plot(x_val,c_data[3],'r--',label="Mid-point_values",marker='o')
        plt.plot(x_val,c_data[5],'y--',label="Raltson_values",marker='o')
        plt.legend(loc='upper center')
        plt.title("Approx. and Exact solutions of ODE")
        #plt.show()

        ##Displaying error graphically:\n
        plt.subplot(1,2,2)
        plt.plot(x_val,c_data[2],'g--',label="RK-3 Method",marker='o')
        plt.plot(x_val,c_data[4],'r--',label="RK-4 Method",marker='o')
        plt.plot(x_val,c_data[6],'y--',label="RK-5 Method",marker='o')
        plt.legend(loc='upper center')
        plt.title("RK-methods-(Error of ODE's)")
        plt.show()

            
else:
    print("Error!!!\nChose option other than specified...")





# -2*x**3+12*x**2-20*x+8.5 y(0)=1 & y(4)=? for h=0.5
# (100+y)/(5*x) y(0.5)=20 & y(1.5)=? for h=0.5 Heun
# (np.exp(x)-2*x)/y => y(0)=1 & y(2)=? for h=0.25
# (1+2*x)*y**0.5 y(0)=1 & y(1)=? for h=0.5
