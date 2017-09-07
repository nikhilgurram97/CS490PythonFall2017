fp=open("para.txt","r")
fi=open("insta.txt","w+")   #opens input and output files respectively
wset={}                        #an empty set initialization
for a in fp.read().split(" "):  #splits the entire paragraphs into words and pushes the words into sets
    if a not in wset:
        wset[a]=1               #Values change to 1
    else:
        wset[a]+=1              #if already existing, 1 value is added
fi.write(str(wset))             #finally, set is written to file
