fp=open("para.txt","r")
fi=open("inst.txt","w+")
wlist2=list()
wlist=fp.read().split(" ")
for i in range(0,len(wlist)):
    wlist2.append("0")
    for j in range(0, len(wlist)):
        if (wlist[i] == wlist[j]):
            wlist2[i]= int(wlist2[i])+1
for l in range(0,len(wlist)):
    fi.write(wlist[l]+" ---> "+str(wlist2[l])+"\n")