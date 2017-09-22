a=input("Enter the limit value n: ")
b={}
for i in range(1,int(a)+1):         #for adding values into dictionary, loop is used
    b[i]=i*i                        #keys and values updated accordingly(square value of keys is updated to value)
print (b)                           #dictionary is printed