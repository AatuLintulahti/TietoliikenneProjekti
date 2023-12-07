import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# funktio k-means klusteroinnin suorittamiseksi
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
final_centroids = k_means(data, num_centroids, iterations=10)

# keskipisteet C-lähdekooditiedostoon
formatted_centroids = "int CP[6][3] = {\n"
for centroid in final_centroids:
    formatted_centroids += "    {" + ", ".join(map(str, centroid)) + "},\n"
formatted_centroids += "};\n"

# tallenna muotoillut keskipisteet 'keskipisteet.h' tiedostoon
header_file_path = 'keskipisteet2.h'  
with open(header_file_path, 'w') as header_file:
    header_file.write(formatted_centroids)

