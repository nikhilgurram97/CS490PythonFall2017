fp=open("para.txt","r")
fi=open("insta.txt","w+")
wset={}
for a in fp.read().split(" "):
    if a not in wset:
        wset[a]=1
    else:
        wset[a]+=1
fi.write(str(wset))