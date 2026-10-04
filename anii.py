import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
n = 3000
theta = np.random.uniform(0, 4 * np.pi, n)
r = np.sqrt(np.random.uniform(0, 1, n))*5
x = r * np.cos(theta) + np.random.normal(0, 0.1, n)
y = r * np.sin(theta) + np.random.normal(0, 0.1, n)

plt.figure(figsize=(8, 8), facecolor='black')
plt.scatter(x, y, s=1, color='cyan',alpha=0.7)
plt.title('ssparkling galaxy', fontsize=14, color='white')
plt.axis('off')
plt.gca().set_facecolor('black')
plt.show()
