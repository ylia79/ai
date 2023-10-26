import matplotlib.pyplot as plt
import numpy as np

balls = np.array([
    [450, 30, 'Basketball'], [200, 10, 'Tennis Ball'], [400, 25, 'Basketball'], [150, 15, 'Tennis Ball'],
    [350, 28, 'Basketball'], [180, 12, 'Tennis Ball'], [500, 32, 'Basketball'], [220, 11, 'Tennis Ball'],
    [420, 27, 'Basketball'], [170, 14, 'Tennis Ball'], [300, 22, 'Unknown']
])

X = balls[:, :2].astype(float)
y = balls[:, 2]
distances = np.sqrt(np.sum((X - [300, 22]) ** 2, axis=1))
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=distances, cmap='viridis', s=100)
plt.colorbar(label='Distance to New Ball')
plt.xlabel('Weight (grams)')
plt.ylabel('Bounce Height (inches)')
nearest_indices = np.argsort(distances)[:2]
for i in nearest_indices:
    plt.annotate(f'{y[i]}', (X[i, 0], X[i, 1]), textcoords="offset points", xytext=(0, 10), ha='center')
plt.scatter(300, 22, marker='*', c='red', s=100, label='New Ball')
plt.legend()
plt.title('Distances Between Balls (Nearest Neighbors Highlighted)')
plt.show()
