inp=input("Enter your string: ")
inp2=list(inp.lower())              #taking input and converting all letters to lowercase, and makiing them to a list
l=len(inp)
alph="abcdefghijklmnopqrstuvwxyz"   #string of all letters of alphabet
alph2=list(alph)                    #converting all alphabet string to list
val=0

for i in range(0,l):                #loop which checks count of availability of alphabets
    for j in range(0,26):
        if (inp2[i]==alph2[j]):
            alph2[j]=0
            val+=1                  #alphabet counter
print ("Contains "+str(val)+" letters of the alphabet, and so")
if(val==26):
    print("Contains all letters of the Alphabet!")
else:
    print("Doesn't contain all letters of the Alphabet!")   #validators where output determines all letters exist or not 
