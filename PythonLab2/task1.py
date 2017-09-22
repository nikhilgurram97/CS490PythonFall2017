inp=input("Enter the sentence:")
inpl=inp.split(" ")             #split function for moving values into array. Considers space as splitting element
inpl=sorted(inpl)               #sorts the newly created array in alphabetical order
inp2=[]
for i in inpl:
    if i not in inp2:
        inp2.append(i)          #removes all duplicates
print(*inp2)                    #printing without array brackets and commas