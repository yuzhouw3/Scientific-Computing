import numpy as np  
import numpy.linalg as la
from tabulate import tabulate


Tfinal = 5
nsteps = [50,100,200,400,800,1600,3200,6400]
yn = []
hn = []


for i in range(8):

    h = Tfinal/nsteps[i]
    hn.append(h)
    hh = h/2
    y = 10.0
    t0 = 0
    for k in range(nsteps[i]):
        y0 = y
        k1 = np.cos(y0*t0)
        y1 = y0 + hh*k1
        t1 = t0+hh
        k2 = np.cos(y1*t1)
        y2 = y0 + hh*k2
        t2 = t0+hh
        k3 = np.cos(y2*t2)
        y3 = y0 + h*k3
        t3 = t0+h
        k4 = np.cos(y3*t3)
        y += h*(k1+2*k2+2*k3+k4)/6

        t0 += h
    yn.append(y)

# table1=[]
# for i in range(8):
#     table1.append([hn[i],yn[i]])
# print(tabulate(table1,headers = ["h_n","y_n"],tablefmt="github",floatfmt=('.15f','.15f',)))


#Part C
table2=[]
#calculate n=25 to get estimate error of n= 50
h=5/25
hh = h/2
y = 10.0
t0 = 0
for k in range(25):
    y0 = y
    k1 = np.cos(y0*t0)
    y1 = y0 + hh*k1
    t1 = t0+hh
    k2 = np.cos(y1*t1)
    y2 = y0 + hh*k2
    t2 = t0+hh
    k3 = np.cos(y2*t2)
    y3 = y0 + h*k3
    t3 = t0+h
    k4 = np.cos(y3*t3)
    y += h*(k1+2*k2+2*k3+k4)/6
    t0 += h
y_25 = y

e = []
e_16 = []
y_hat=[]

for i in range(8):
    if i==0:
        e.append((1/15)*(yn[0]-y_25))
    else:       
        e.append((1/15)*(yn[i]-yn[i-1]))
    
    e_16.append(e[i]/16)
    y_hat.append(yn[i]+e[i])

for i in range(8):
    table2.append([nsteps[i],hn[i],yn[i],y_hat[i],e[i],e_16[i]])
print(tabulate(table2,headers = ["n","h_n","y_n","y^_n","e_est,n","1/16e_est,n"],tablefmt="github",floatfmt=('.0f','.15f','.15f','.15f','.15f','.15f')))
