import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(6, 6))
walls = plt.Rectangle((-1.5, -1.5), 3, 2.5, color='powderblue', linewidth=2)
ax.add_patch(walls)
roof = plt.Polygon([[-1.8, 1], [1.8, 1], [0, 2.5]], color='magenta')
ax.add_patch(roof)
door = plt.Rectangle((-0.4, -1.5), 0.8,1.2, color='saddlebrown')
ax.add_patch(door)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2, 3)
plt.title('Small House Shape', fontsize=14)
plt.axis('off')
plt.show()