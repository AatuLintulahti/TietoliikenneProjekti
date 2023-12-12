import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# funktio k-means klusteroinnin suorittamiseksi
'''
def k_means(data, num_centroids, iterations):
    np.random.seed(0)  # alkutila toistettavuuden varmistamiseksi
    min_values = np.min(data, axis=0)
    max_values = np.max(data, axis=0)
    centroids = np.random.uniform(min_values, max_values, (num_centroids, 3))

    for _ in range(iterations):
        distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
        nearest_centroids = np.argmin(distances, axis=0)

        for i in range(num_centroids):
            points_assigned_to_centroid = data[nearest_centroids == i]
            if points_assigned_to_centroid.size:
                centroids[i] = np.mean(points_assigned_to_centroid, axis=0)

    return centroids

'''
def k_means(data, num_centroids, iterations):
    min_values = np.min(data, axis=0)
    max_values = np.max(data, axis=0)
    centroids = np.random.uniform(0, max_values, (num_centroids, 3))
    cumSum = np.zeros((6,3))
    counts = np.zeros([1,6])
    distance = [0,0,0,0,0,0]
    for _ in range(iterations):
        for i in data:
            for j in range(6):
                distance[j] = np.linalg.norm(i-centroids[j])
            print (i)
            print(distance)
            winner = np.argmin(distance)
            cumSum[winner] += i
            #np.insert(cumSum,winner,i, axis=0)
            counts[0,winner] += 1
        print (counts)
        print (centroids)
        for x in range(centroids.shape[0]):
            if counts[0,x] <= 3:
                centroids[x] = np.random.uniform(min_values, max_values, (1, 3))
            else:
                for y in range(3):
                    centroids[x,y]=cumSum[x,y] / counts[0,x]
        if _ < iterations - 1:
            cumSum *=0
            counts *=0


    return centroids


# lataa kiihtyvyysanturin data  
data = np.loadtxt('data.txt', delimiter=';', usecols=(6, 7, 8))

# data 3D-hajontakaaviona
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of Accelerometer Data')
plt.show()

# pyöritä K-means algoritmi
num_centroids = 6  
final_centroids = k_means(data, num_centroids, iterations=1000)
print(final_centroids)
# järjestä keskipisteet
max_x = np.argmax(final_centroids[:, 0])
min_x = np.argmin(final_centroids[:, 0])
max_y = np.argmax(final_centroids[:, 1])
min_y = np.argmin(final_centroids[:, 1])
max_z = np.argmax(final_centroids[:, 2])
min_z = np.argmin(final_centroids[:, 2])

max_x_row = np.take(final_centroids, max_x, axis=0)
min_x_row = np.take(final_centroids, min_x, axis=0)
max_y_row = np.take(final_centroids, max_y, axis=0)
min_y_row = np.take(final_centroids, min_y, axis=0)
max_z_row = np.take(final_centroids, max_z, axis=0)
min_z_row = np.take(final_centroids, min_z, axis=0)


final_final_centroids = np.vstack((max_x_row, min_x_row, max_y_row, min_y_row, max_z_row, min_z_row))

# keskipisteet C-lähdekooditiedostoon
print (final_final_centroids)
formatted_centroids = "int CP[6][3] = {\n"
for centroid in final_final_centroids:
    formatted_centroids += "    {" + ", ".join(map(str, centroid)) + "},\n"
formatted_centroids += "};\n"

# tallenna muotoillut keskipisteet 'keskipisteet.h' tiedostoon
header_file_path = 'keskipisteet2.h'  
with open(header_file_path, 'w') as header_file:
    header_file.write(formatted_centroids)

