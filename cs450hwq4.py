import numpy as np 
import scipy as sp 
import numpy.linalg as la
import matplotlib.pyplot as plt
from tabulate import tabulate

# composite trapezoid for uniformlt points to evaluate f(x,y) = e^(x+y) on [0,2]X[0,1]
def Qct1(n):
    xline = np.linspace(0,2,n+1)
    yline = np.linspace(0,1,n+1)
    
    result = 0

    for xi in xline:
        if xi == 0 or xi==2:
            w_xi = 1/n
        else:
            w_xi = 2/n
        for yj in yline:
            if yj == 0 or yj == 1:
                w_yj = 1/(2*n)
            else:
                w_yj = 1/n
            result += w_xi*w_yj*np.exp(xi+yj)
    return result

# composite trapezoid for uniformlt points to evaluate f(x,y) = e^(x*y) on [0,2]X[0,1]
def Qct2(n):
    xline = np.linspace(0,2,n+1)
    yline = np.linspace(0,1,n+1)
    
    result = 0

    for xi in xline:
        if xi == 0 or xi==2:
            w_xi = 1/n
        else:
            w_xi = 2/n
        for yj in yline:
            if yj == 0 or yj == 1:
                w_yj = 1/(2*n)
            else:
                w_yj = 1/n
            result += w_xi*w_yj*np.exp(xi*yj)
    return result

ns = []
er1 = []
er2 = []
for i in range(7):
    ns.append(2**(i+1))
ns = np.array(ns)
real_result = (np.exp(2)-1)*(np.exp(1)-1)

for n in ns:
    er1.append(np.absolute(real_result-Qct1(n)))
er1 = np.array(er1)

# compute Richardson Extrapolation
rich_ex = []
for n in ns:
    rich_ex.append(Qct1(2*n)*4/3-Qct1(n)/3)

for value in rich_ex:
    er2.append(np.absolute(real_result-value))
er2 = np.array(er2)

plt.figure()
plt.loglog(ns,er1,label = 'composite trapezoid')
plt.loglog(ns,er2,label = 'Richardson Extrapolation')
plt.title("Error of |I-Qct| as function of n")
plt.legend()
plt.show()


rich_ex2 = []
qct = []
for n in ns:
    qct.append(Qct2(n))
    rich_ex2.append(Qct2(2*n)*4/3-Qct2(n)/3)

table=[]
for i in range(ns.size):
    table.append([ns[i],qct[i],rich_ex2[i]])
print(tabulate(table,headers = ["n","QCT(n)","Richardson(n)"],tablefmt="github",floatfmt=('.0f','.15f','.15f',)))