import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import gaussian_kde
from matplotlib.colors import LogNorm
#%matplotlib inline
#from sklearn.datasets.samples_generator import make_blobs
#X, y = make_blobs(n_samples=100, n_features=3, centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2], random_state =9)
#fig = plt.figure()
#ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
#plt.scatter(X[:, 0], X[:, 1], X[:, 2],marker='o')

#print X
from sklearn.decomposition import PCA
#pca = PCA(n_components=3)
#pca.fit(X)
#print pca.explained_variance_ratio_
#print pca.explained_variance_


#pca = PCA(n_components=2)
#pca.fit(X)
#print pca.explained_variance_ratio_
#print pca.explained_variance_
#print X
data = open('qresult.txt','r')

#for line in data.readlines()
#  line = line.strip()

fname=[]
allnum=[]
everynum=[]
for i in range(3051):
#    for j in range(6):
      everynum=[]
      everystr=[]
      fname.append(data.readline().strip())
      everystr.extend(data.readline().split())
      everystr.extend(data.readline().split())
#      data.readline()
      everystr.extend(data.readline().split())
#      data.readline()
      for num in everystr:  
        everynum.append(float(num))
      allnum.append(everynum)

data.close()

#print allnum

pca = PCA(n_components=2)
pca.fit(allnum)
#print pca.explained_variance_ratio_
#print pca.explained_variance_
#print X

numnew = pca.transform(allnum)

x = numnew[:, 0]
y = numnew[:, 1]


#plt.hist2d(x, y, bins=100, norm=LogNorm())

#plt.colorbar()
#plt.show()

xy = np.vstack([x,y])

z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()

ax.scatter(x, y, c=z, s=50, edgecolor='',marker='x')
#plt.colorbar()
plt.show()
#plt.scatter(numnew[:, 0], numnew[:, 1],marker='o')
#plt.show()




#fig = plt.figure()
#ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
#plt.scatter(numnew[:, 0], numnew[:, 1], numnew[:, 2],marker='o')

#print len(numnew)


#print numnew[0]
k=0
data2 = open('SortStructure.txt','w')
for num2 in numnew:
    data2.write(fname[k])
    k=k+1
    data2.write('\n')
    for num4 in num2:
      num3 = str(num4)
      data2.write(num3)
      data2.write('  ')
    data2.write('\n')

data2.close()

