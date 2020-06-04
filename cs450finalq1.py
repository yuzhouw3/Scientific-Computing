import numpy as np
import scipy as sp
from scipy.sparse import diags
from scipy import linalg
#import matplotlib.pyplot as plt

# part a
n=160
sigma = 1

# #part b
# n=27
# sigma = 3.507


# h = 1/n
# A = (1/(h*h))*diags([-1, 2, -1], [-1, 0, 1], shape=(n-1, n-1)).toarray()

# u = np.zeros(n-1)
# b = np.ones(n-1)
# x = []
# x_p = []
# for i in range(1,n):
#   x.append(i)
#   x_p.append(i/n)
# x = np.array(x)
# x_p = np.array(x_p)

# c = -2*b+sigma*h*h*np.exp(x_p)
# J = (1/(h*h))*diags([(-1)*b,(-1)*c,(-1)*b],[-1,0,1],shape=(n-1,n-1)).toarray()
# it = 0
# error =1

# while error>=1e-9:
#   f = A@u-sigma*np.exp(u)
#   c = -2*b + sigma*h*h*np.exp(u)
#   J = (1/(h*h))*diags([(-1)*b,(-1)*c,(-1)*b],[-1,0,1],shape=(n-1,n-1)).toarray()
#   try:
#     P,L,U = sp.linalg.lu(J)
#   except:
#       print("Diverge")
#       break
#   s = np.linalg.solve((-1)*U,np.linalg.solve(L,f))
#   u=u+s
#   error = np.linalg.norm(f)
#   it+=1

# print(it-1)
# print(u[0]/h)



# plt.plot(x, u, 'r-')
# plt.xlabel('x')
# plt.ylabel('u')

dudx = [0.8481386777020908,0.8607107619278902,0.8669787798609137,0.8701082841490002]
#dudx = [0.5242512354851435,0.5368273618242253,0.543096387435477,0.5462261434651918]
ri = []
for i in range(3):
    ri.append(2*dudx[i+1]-dudx[i])
print(ri)

print(ri[1]-ri[0])
print(ri[2]-ri[1])
