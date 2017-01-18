import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def f1(x):
    return np.abs(x)**0.25
def f1p(x):
    return 0.25*np.sign(x)*(np.abs(x)**(-0.75))

def f2(x):
    return np.abs(x)**0.75
def f2p(x):
    return 0.75*np.sign(x)*(np.abs(x)**(-0.25))

print("f1 Newton's:")
try:
    print("f1 root: ", opt.newton(f1,0.5,f1p))
except RuntimeError as e:
    print(e)

print("f2 Newton's:")
try:
    print("f2 root: ", opt.newton(f2,0.5,f2p))
except RuntimeError as e:
    print(e)

plt.subplot(2, 1, 1)
x = np.linspace(-1,1,1001)
plt.plot(x,f1(x),label="$|x|^{0.25}$")
plt.plot(x,f2(x),label="$|x|^{0.75}$")
plt.plot(x,0*x,color="k",linestyle="--")
plt.ylim(-0.1,1)
plt.legend(loc="best")


def f3(x):
    return 5*np.sin(x)/(x-1)+1
def f3p(x):
    return (5*(x-1)*np.cos(x) - 5*np.sin(x))/(x-1)**2

print("f3 Newton's:")
try:
    print("f3 root x0 = 1.01: ", opt.newton(f3,1.01,f3p))
    print("f3 root x0 = 6   : ", opt.newton(f3,6,f3p))
    print("f3 root x0 = 11  : ", opt.newton(f3,11,f3p))
except RuntimeError as e:
    print(e)

print("f3 Bisection:")
try:
    print("f3 root [1.01,4 ]  : ", opt.bisect(f3,1.01,4))
    print("f3 root [4   ,10]  : ", opt.bisect(f3,4,10))
except RuntimeError as e:
    print(e)

print("f3 Brent:")
try:
    print("f3 root [1.01,4 ]  : ", opt.brentq(f3,1.01,4))
    print("f3 root [4   ,10]  : ", opt.brentq(f3,4,10))
except RuntimeError as e:
    print(e)


plt.subplot(2, 1, 2)
x = np.linspace(1.0001, 20)
plt.plot(x,f3(x),label="$5 \sin x / (x-1) + 1$")
plt.plot(x,0*x,color="k",linestyle="--")
plt.ylim(-1,5)
plt.legend(loc="best")

plt.savefig("plots.png")
plt.show()
