import numpy as n
a=n.random.rand(15)                                     #random function to generate 15 random values into a list
print("Previous Vector: ")
print(a)
b=max(a)                                                #finding max value in the generated vector
for i in range(15):                                     #loop to replace largest value with 100
    if a[i]==b:
        a[i]=100
        c=i
print("\nMax Value: "+str(b)+", At Index "+str(c+1))
print("\nNew Vector: (Replacing Index "+str(c+1)+")")
print(a)                                                #newly generated vector