inp=input("Enter your string: ")
inp2=list(inp.lower())
l=len(inp)
alph="abcdefghijklmnopqrstuvwxyz"
alph2=list(alph)
val=0

for i in range(0,l):
    for j in range(0,26):
        if (inp2[i]==alph2[j]):
            alph2[j]=0
            val+=1
print ("Contains "+str(val)+" letters of the alphabet, and so")
if(val==26):
    print("Contains all letters of the Alphabet!")
else:
    print("Doesn't contain all letters of the Alphabet!")
