from scipy.integrate import odeint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sympy as sp

a2,a1,p1,q11=sp.symbols("a1 a2 p1 q11")

e1=sp.Eq(a1+a2,1)
e2=sp.Eq(a2*p1,1/2)
e3=sp.Eq(a2*q11,1/2)


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



#For RK-2nd -Order methods Heun , Mid-points , Raltson's methods
##################################################
a2_list=[1/2,1,2/3]
for z in range(3):
    val_a2=a2_list[z]
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
##################################################

for j in range(3):
    for i in range(int(n)+1):

        if j==0:#For RK-3 method
            #print("I'm in RK-3")
            k1=f(val,yo_h)
            k2=f(val+(1/2)*h , yo_h+(1/2)*k1*h)
            k3=f(val+h , yo_h-k1*h+2*k2*h)
            thita = (k1+4*k2+k3)/6
            ##
            #print("\nFor run = ",i+1," in j = ",j+1,"RK-3")
            #print("k1 = ",k1*h,"\nk2 = ",k2*h,"\nk3 = ",k3*h,"\nthita = ",thita*h)
            y_new = yo_h + thita*h
            data.append(y_new)
            
        elif j==1:#For RK-4 method
            #print("I'm in RK-4")
            k1=f(val,yo_h)
            k2=f(val+(1/2)*h , yo_h+(1/2)*k1*h)
            k3=f(val+(1/2)*h , yo_h+(1/2)*k2*h)
            k4=f(val+h , yo_h+k3*h)
            thita = (k1+2*k2+2*k3+k4)/6
            ##
            #print("\nFor run = ",i+1," in j = ",j+1,"RK-4")
            #print("k1 = ",k1*h,"\nk2 = ",k2*h,"\nk3 = ",k3*h,"\nk4 = ",k4*h,"\nthita = ",thita*h,"\n")
            y_new = yo_h + thita*h
            data.append(y_new)

        elif j==2:#For RK-5-Butcher method
            #print("I'm in RK-5")
            k1=f(val,yo_h)
            k2=f(val+(1/4)*h , yo_h+(1/4)*k1*h)
            k3=f(val+(1/4)*h , yo_h+(1/8)*k1*h+(1/8)*k2*h)
            k4=f(val+(1/2)*h , yo_h-(1/2)*k2*h+k3*h)
            k5=f(val+(3/4)*h , yo_h+(3/16)*k1*h+(9/16)*k4*h)
            k6=f(val+h , yo_h-(3/7)*k1*h+(2/7)*k2*h+(12/7)*k3*h-(12/7)*k4*h+(8/7)*k5*h)
            thita = (7*k1+32*k3+12*k4+32*k5+7*k6)/90
            ##
            #print("\nFor run = ",i+1," in j = ",j+1,"RK-5")
            #print("k1 = ",k1*h,"\nk2 = ",k2*h,"\nk3 = ",k3*h,"\nk4 = ",k4*h,"\nk5 = ",k5*h,"\nk6 = ",k6*h,"\nthita = ",thita*h,"\n")
            y_new = yo_h + thita*h
            data.append(y_new)

        yo_h=y_new
        val+=h
        
    else:
        #data_correction
        data.insert(0,yo)
        data.pop()
        print(len(data))
        ##
        for i in range(int(n)+1):
            #error calculation
            error=(abs(data[i]-true_val[i])/true_val[i])*100
            error_val.append(error)
            #error
        
        c_data.append(data)
        data=[]
        c_data.append(error_val)
        error_val=[]

        val=a
        yo_h=yo
        
else:
    ##Displaying data numerically:
    #pd.set_option('display.max_columns',7)
    pd.set_option('display.max_columns',30)
    panda_data=pd.DataFrame(c_data)
    panda_data=panda_data.T
    panda_data.columns=["y_true","y_heun" , "Heun_error" , "y_mid-point" , "Mid_error" , "y_raltson","Raltson_error","RK-3","RK-3 Error(%)","RK-4","RK-4 Error(%)","RK-5","RK-5 Error(%)"]
    panda_data.index=x_val
    print(panda_data)

    ##Displaying data graphically:\n
    plt.subplot(1,2,1)
    plt.plot(x_val,c_data[0],'b--',label="True_values",marker='o')
    plt.plot(x_val,c_data[1],'g--',label="RK-2 Heun Method",marker='o')
    plt.plot(x_val,c_data[3],'r--',label="RK-2 Mid-point Method",marker='o')
    plt.plot(x_val,c_data[5],'y--',label="RK-2 Raltson's Method",marker='o')
    plt.plot(x_val,c_data[7],'m--',label="RK-3 Method",marker='o')
    plt.plot(x_val,c_data[9],'c--',label="RK-4 Method",marker='o')
    plt.plot(x_val,c_data[11],'k--',label="RK-5 Method",marker='o')
    plt.legend(loc='upper center')
    plt.title("RK-methods-(solutions of ODE's)")
    #plt.show()

    ##Displaying error graphically:\n
    plt.subplot(1,2,2)
    plt.plot(x_val,c_data[2],'g--',label="RK-2 Heun Method",marker='o')
    plt.plot(x_val,c_data[4],'r--',label="RK-2 Mid-point Method",marker='o')
    plt.plot(x_val,c_data[6],'y--',label="RK-2 Raltson Method",marker='o')
    plt.plot(x_val,c_data[8],'m--',label="RK-3 Method",marker='o')
    plt.plot(x_val,c_data[10],'c--',label="RK-4 Method",marker='o')
    plt.plot(x_val,c_data[12],'k--',label="RK-5 Method",marker='o')
    plt.legend(loc='upper center')
    plt.title("RK-methods-(Error of ODE's)")
    plt.show()


#-2*x**3+12*x**2-20*x+8.5
#y(0)=1 & y(4)=? for h=0.5
# (100+y)/(5*x) y(0.5)=20 & y(1.5)=? for h=0.5 Heun
# (np.exp(x)-2*x)/y => y(0)=1 & y(2)=? for h=0.25
# (1+2*x)*y**0.5 y(0)=1 & y(1)=? for h=0.5



# 3*np.exp(-x)-0.4
# 4*np.exp(0.8*x)-0.5*y
# y(0)=5
# y(3)=? for h=1.5
