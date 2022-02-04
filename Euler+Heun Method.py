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

y_predictor=0
y_=0
yo_e=yo
yo_h=yo
e_val_predictor=[]
e_val_corrector=[]
def derivative(y,x):
    return eval(exp)

def solve(x,yo):
    return odeint(derivative,yo,x)


def f(x,y):
    re=eval(exp)
    return re


error_Euler=[]
error_Heun=[]

for i in range(int(n)+1):
    x_val.append(val)
    y_predictor=yo_e + h*f(val,yo_e)
    e_val_predictor.append(y_predictor)
    #
    y_corrector = yo_h + h*((f(val,yo_h)+f(val+h,y_predictor))/2)
    e_val_corrector.append(y_corrector)
    #
    val+=h
    yo_h = y_corrector
    yo_e = y_predictor
    
    
else:
    true_val=solve(x_val,yo)
    true_val=true_val.ravel()
    #
    e_val_predictor.insert(0,yo)
    e_val_predictor.pop()
    ##
    e_val_corrector.insert(0,yo)
    e_val_corrector.pop()
    #
    for i in range(int(n)+1):
        ##calculation of true value
        error=(abs(e_val_predictor[i]-true_val[i])/true_val[i])*100
        error_Euler.append(error)
        #
        error=(abs(e_val_corrector[i]-true_val[i])/true_val[i])*100
        error_Heun.append(error)
    #
    dic1={
        "y_true":true_val,
        "y_euler":e_val_predictor,
        "y_Heun":e_val_corrector,
        "error_Euler(%)":error_Euler,
        "error_Heun(%)":error_Heun
        }
    data=pd.DataFrame(dic1,index=x_val)
    print(data)
    plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
    plt.plot(x_val,e_val_predictor,'g--',label="Euler_values",marker='o')
    plt.plot(x_val,e_val_corrector,'r--',label="Heun_values",marker='o')
    plt.legend(loc='upper center')
    plt.show()

# -2*x**3+12*x**2-20*x+8.5 y(0)=1 & y(4)=? for h=0.5
# (100+y)/(5*x) y(0.5)=20 & y(1.5)=? for h=0.5 Heun
# (np.exp(x)-2*x)/y => y(0)=1 & y(2)=? for h=0.25
