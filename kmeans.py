import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x,y))
inertias = {}
num_clusts = 0

for i in range(1,11):
    try:
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        inertias[str(kmeans.inertia_)]=i
    except:
        print("uhoh")
for i in range(1,len(inertias)):
    inerts = list(inertias.keys())
    inert = inerts[i-1]
    if  float(inerts[i]) > ((float(inert)/2)): #Can either do this as if current is < previous/x then return current OR if current is > previous/z then return previous
        #This way seems to work better
        num_clusts = inertias.get(inert)
        print(num_clusts)
        break



kmeans = KMeans(n_clusters=num_clusts)
kmeans.fit(data)

labeled_data = list(zip(data,kmeans.labels_))
for lab in labeled_data:
    print(lab)

plt.scatter(x,y,c=kmeans.labels_)
plt.show()