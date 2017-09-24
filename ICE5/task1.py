import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])

xb=np.mean(x)
yb=np.mean(y)

xn=x-xb
yn=y-yb

num=sum(xn*yn)
den=sum(xn*xn)

slope=num/den

incp=yb-slope*xb

print("Slope: "+str(slope)+"\nY Intercept: "+str(incp))

plt.scatter(x,y,)

plt.plot(x,slope*x+incp,'r')
plt.show()