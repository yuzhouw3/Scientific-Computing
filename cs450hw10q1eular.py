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
    y = 10.0
    t0 = 0
    for k in range(nsteps[i]):
        y0 = y
        k = np.cos(y0*t0)
        y += h*k
        t0 += h
    yn.append(y)


#Part C
table=[]
#calculate n=25 to get estimate error of n= 50
h=5/25
y = 10.0
t0 = 0
for k in range(25):
    y0 = y
    k = np.cos(y0*t0)
    y += h*k
    t0 += h
y_25 = y

e = []
e_2 = []
y_hat=[]

for i in range(8):
    if i==0:
        e.append((yn[0]-y_25))
    else:       
        e.append((yn[i]-yn[i-1]))
    
    e_2.append(e[i]/2)
    y_hat.append(yn[i]+e[i])

for i in range(8):
    table.append([nsteps[i],hn[i],yn[i],y_hat[i],e[i],e_2[i]])
print(tabulate(table,headers = ["n","h_n","y_n","y^_n","e_est,n","1/2e_est,n"],tablefmt="github",floatfmt=('.0f','.15f','.15f','.15f','.15f','.15f')))
