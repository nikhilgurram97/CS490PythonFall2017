from sklearn.cluster import KMeans
import pandas
import matplotlib.pyplot as p               #importing all necessary libraries

da = pandas.read_csv('cust.csv',header=0)   #reading the CSV Input
d=da.as_matrix(columns=None)                #pandas interpretation to form a numpy array from csv file
k = KMeans(n_clusters=5, random_state=0)    #Initializing KMeans
k.fit(da)                                   #Training data to compute clustering
labels=k.labels_                            #labels array
centroid=k.cluster_centers_                 #centroid points
colors = ["r.","g.","b.","c.","y."]         #colors to differtnate clusters

for i in range(len(d)):
   p.plot(d[i][0],d[i][1],colors[labels[i]],markersize=10)  #plotting points

p.scatter(centroid[:,0],centroid[:,1], marker = ".", s=150, linewidths = 5, zorder =10,color='yellow')     #plotting centroids
p.show()                                                                                    #displaying plot