import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dati frequenze per intervallo
data = [
    ((1250, 2500), (2500, 3750), 1),
    ((2500, 3750), (2500, 3750), 3),
    ((3750, 5000), (2500, 3750), 1),
    ((3750, 5000), (3750, 5000), 2),
    ((5000, 6250), (3750, 5000), 3),
    ((6250, 7500), (3750, 5000), 1),
    ((5000, 6250), (5000, 6250), 2),
    ((6250, 7500), (5000, 6250), 1),
    ((6250, 7500), (6250, 7500), 2),
    ((7500, 8750), (6250, 7500), 2)
]

# Coordinate al centro dei range
x_centers = [ (x1+x2)/2 for (x1, x2), _, _ in data ]
y_centers = [ (y1+y2)/2 for _, (y1, y2), _ in data ]
frequencies = np.array([ f for _, _, f in data ])

# Parametri dimensione barre
dx = dy = 1000
dz = frequencies

# Normalizzazione colori
norm = plt.Normalize(frequencies.min(), frequencies.max())
colors = plt.cm.viridis(norm(frequencies))

# Creazione grafico 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

bars = ax.bar3d(x_centers, y_centers, np.zeros_like(dz), dx, dy, dz, 
                color=colors, shade=True, edgecolor='black', linewidth=0.6)

# Barra dei colori
mappable = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
mappable.set_array(frequencies)
fig.colorbar(mappable, ax=ax, shrink=0.6, label='Frequenza')

# Etichette e titolo
ax.set_xlabel('Packets sent', labelpad=12)
ax.set_ylabel('Packets received', labelpad=12)
ax.set_zlabel('Frequency', labelpad=10)
ax.set_title('3D Histogram of Packet Correlations', pad=20)

# Tick sugli assi
ax.set_xticks(np.arange(0, 10001, 1250))
ax.set_yticks(np.arange(0, 10001, 1250))
ax.set_zticks(np.arange(0, max(frequencies)+1, 1))

# Miglioramenti estetici
ax.view_init(elev=25, azim=130)  # angolo visuale più leggibile
ax.grid(True)

plt.tight_layout()
plt.show()
