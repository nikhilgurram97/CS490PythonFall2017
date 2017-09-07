fp=open("para.txt","r")
fi=open("inst.txt","w+")    #opens input and output files respectively
wlist2=list()               #initializes list
wlist=fp.read().split(" ")  #splits entire paragraphs into words and pushes them into list
for i in range(0,len(wlist)):   
    wlist2.append("0")          #appends a 0 to wlist2 for every occurence of wlist
    for j in range(0, len(wlist)):
        if (wlist[i] == wlist[j]):  
            wlist2[i]= int(wlist2[i])+1     #Adds 1 to corresponding wlsit2 value of wlist1, if there is a word occurence for another time
for l in range(0,len(wlist)):
    fi.write(wlist[l]+" ---> "+str(wlist2[l])+"\n") #Writes the output to the output file
