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
    #print(true_val)
    c_data.append(true_val)
###########################

##definition of slopes
def f(x,y):
    return eval(exp)


for i in range(int(n)+1):
    k1=f(val,yo_h)
    k2=f(val+(1/2)*h , yo_h+(1/2)*k1*h)
    k3=f(val+h , yo_h-k1*h+2*k2*h)
    thita = (k1+4*k2+k3)/6
    ##
    print("k1 = ",k1*h,"\nk2 = ",k2*h,"\nk3 = ",k3*h,"\nthita = ",thita*h)
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
        panda_data.columns=["y_true","RK-3rd-Order" , "error(%)"]
        panda_data.index=x_val
        print(panda_data)

        ##Displaying data graphically:\n
        plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
        plt.plot(x_val,data,'g--',label="RK-3rd-Order",marker='o')
        plt.legend(loc='upper center')
        plt.title("RK-methods solutions of ODE's")
        plt.show()


# -2*x**3+12*x**2-20*x+8.5 y(0)=1 & y(4)=? for h=0.5
# (100+y)/(5*x) y(0.5)=20 & y(1.5)=? for h=0.5 Heun
# (np.exp(x)-2*x)/y => y(0)=1 & y(2)=? for h=0.25
# (1+2*x)*y**0.5 y(0)=1 & y(1)=? for h=0.5
