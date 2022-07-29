

#Trapezoidal function call variable step

import numpy as np
from scipy.integrate import trapz
from scipy.integrate import quad
from scipy.integrate import quadrature
from scipy.integrate import fixed_quad

def f(x):
    return np.sin(x)
n=2
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
xs,h=np.linspace(a,b,n,retstep=True)
ys= np.sin(xs)
i=(h/2)*(ys[0]+ys[-1])
i1=0
while(abs(i-i1)>1.0e-6):
    i1=i
    n=n+1
    xs,h=np.linspace(a,b,n,retstep=True)
    ys= np.sin(xs)
    i=(h/2)*(ys[0]+ys[-1]+2*np.sum(ys[1:-1:1]))

print("no.of iteration: ",(n-2))
print("Trapezoidal rule integrated result: ",i)
print("scipy based Trapezoidal rule integrated result: : ",trapz(ys,dx=h))
print("general purpose integration: ",quad(f,a,b))
print("quadrature(general with fixed tolerance): ",quadrature(f,a,b,tol=1.0e-5))
print("general quadrature with fixed order: ",fixed_quad(f,a,b,n=2))
