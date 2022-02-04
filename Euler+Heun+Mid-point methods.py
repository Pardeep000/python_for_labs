from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

exp=input("f(x,y) = ")

a=float(input("initial x-value: "))
b=float(input("final x-value: "))
yo=float(input("initial y-value: "))
h=float(input("step size: "))
n=int((b-a)/h)

val=a

x_val=[]


y_predictor=0
yo_e=yo
yo_h=yo
yo_m=yo

e_val_predictor=[]
e_val_corrector=[]
e_val_mid=[]


error_Euler=[]
error_Heun=[]
error_Mid=[]



#For True values / Analytical solutions
#############################
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
    #c_data.append(true_val)
#############################


#Definition of functions for slopes at particular points
def f(x,y):
    re=eval(exp)
    return re


for i in range(int(n)+1):
    ## Euler +Heun
    y_predictor=yo_e + h*f(val,yo_e)
    e_val_predictor.append(y_predictor)
    ## Heun
    y_corrector = yo_h + h*((f(val,yo_h)+f(val+h,y_predictor))/2)
    e_val_corrector.append(y_corrector)
    ## Mid-point values
    y_mid = yo_m + (h/2)*f(val,yo_m)
    y_full = yo_m + (h)*f(val+(h/2),y_mid)
    e_val_mid.append(y_full)
    ##
    val+=h #as x- value e.g 'xo'
    yo_h = y_corrector
    yo_e = y_predictor
    yo_m=y_full
    
else:
    e_val_predictor.insert(0,yo)
    e_val_predictor.pop()
    ##
    e_val_corrector.insert(0,yo)
    e_val_corrector.pop()
    ##
    e_val_mid.insert(0,yo)
    e_val_mid.pop()
    #
    for i in range(int(n)+1):
        ##calculation of true value
        error=(abs(e_val_predictor[i]-true_val[i])/true_val[i])*100
        error_Euler.append(error)
        #
        error=(abs(e_val_corrector[i]-true_val[i])/true_val[i])*100
        error_Heun.append(error)
        #
        error=(abs(e_val_mid[i]-true_val[i])/true_val[i])*100
        error_Mid.append(error)
    #
    dic1={
        "y_true":true_val,
        "y_euler":e_val_predictor,
        "y_Heun":e_val_corrector,
        "y_Mid":e_val_mid,
        "error_Euler(%)":error_Euler,
        "error_Heun(%)":error_Heun,
        "error_Mid(%)":error_Mid
        }
    pd.set_option('display.max_columns',7)
    data=pd.DataFrame(dic1,index=x_val)
    print(data)
    #
    plt.subplot(2,1,1)
    plt.plot(x_val,true_val,'b--',label="True_values",marker='o')
    plt.plot(x_val,e_val_predictor,'g--',label="Euler_values",marker='o')
    plt.plot(x_val,e_val_corrector,'r--',label="Heun_values",marker='o')
    plt.plot(x_val,e_val_mid,'y--',label="Mid_values",marker='o')
    plt.legend(loc='upper center')
    plt.title("Approx. and Exact solutions of ODE")
    #plt.show()

    plt.subplot(2,1,2)
    plt.plot(x_val,error_Euler,'g--',label="Euler_values",marker='o')
    plt.plot(x_val,error_Heun,'r--',label="Heun_values",marker='o')
    plt.plot(x_val,error_Mid,'y--',label="Mid_values",marker='o')
    plt.legend(loc='upper center')
    plt.title("Errors of solutions of ODE")
    plt.show()

# -2*x**3+12*x**2-20*x+8.5 y(0)=1 & y(4)=? for h=0.5
# (100+y)/(5*x) y(0.5)=20 & y(1.5)=? for h=0.5 Heun
# (np.exp(x)-2*x)/y => y(0)=1 & y(2)=? for h=0.25
# (1+2*x)*y**0.5 y(0)=1 & y(1)=? for h=0.5
