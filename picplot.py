import numpy as np
import matplotlib.pyplot as plt

data = open('EpairD.txt','r')

#for line in data.readlines()
#  line = line.strip()

#fname=[]
allnum=[]
everynum=[]
x = []
y = []
for i in range(3000):
#    for j in range(6):
      everynum=[]
      everystr=[]
#      fname.append(data.readline().strip())
      everystr.extend(data.readline().split())
#      everystr.extend(data.readline().split())
#      data.readline()
#      everystr.extend(data.readline().split())
#      data.readline()
      for num in everystr:
        everynum.append(float(num))
      x.append(everynum[0])
      y.append(everynum[1])
      allnum.append(everynum)

data.close()

#print allnum
#x = []
#y = []

#for i in range(3000):
#  x.append(allnum[i,0])
#  y.append(allnum[i,1])

#print x


plt.scatter(x, y,s=10,marker='+')
plt.show()




