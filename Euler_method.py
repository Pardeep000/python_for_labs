from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x_val=[]
exp=input("f(x,y) = ")

a=float(input("initial x-value: "))
b=float(input("final x-value: "))
yo=float(input("initial y-value: "))
h=float(input("step size: "))
n=int((b-a)/h)
#n+=1

val=a

y_new=0
yo_e=yo
e_val=[]
def derivative(y,x):
    return eval(exp)

def solve(x,yo):
    return odeint(derivative,yo,x)


def func_val(x,y):
    re=eval(exp)
    return re


error_val=[]

for i in range(int(n)+1):
    x_val.append(val)
    y_new=yo_e + h*func_val(val,yo_e)
    e_val.append(y_new)
    #
    val+=h
    yo_e=y_new
    
else:
    true_val=solve(x_val,yo)
    true_val=true_val.ravel()
    #
    e_val.insert(0,yo)
    e_val.pop()
    #
    for i in range(int(n)+1):
        ##calculation of true value
        error=(abs(e_val[i]-true_val[i])/true_val[i])*100
        error_val.append(error)
    #
    dic1={
        "y_true":true_val,
        "y_euler":e_val,
        "error (%)":error_val
        }
    data=pd.DataFrame(dic1,index=x_val)
    print(data)
    plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
    plt.plot(x_val,e_val,'g--',label="Euler_values",marker='o')
    plt.legend(loc='upper center')
    plt.show()

#-2*x**3+12*x**2-20*x+8.5
#
