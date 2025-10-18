import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__=="__main__":
    # Parametri
    n = 30      # Dimensione del campione
    k = 5000    # Numero di campioni
    a = np.random.exponential(scale=4, size=10000)  # Popolazione non normale con andamento esponenziale

    # Calcolo delle medie campionarie
    sample_means = [np.mean(np.random.choice(a, size=n, replace=True)) for _ in range(k)]

    # Statistiche
    mu = np.mean(a)
    sigma = np.std(a) / np.sqrt(n)

   # Figure setup
    plt.figure(figsize=(10,8))

    # ---- Plot 1: Popolazione originale ----
    plt.subplot(2,1,1)
    plt.hist(a, bins=50, color='skyblue', edgecolor='black', density=True)
    plt.title(f"Popolazione - Distribuzione non normale (Media = {np.mean(a):.2f}, σ = {np.std(a):.2f})")

    # ---- Plot 2: Distribuzione delle medie campionarie con gaussiana ----
    plt.subplot(2,1,2)
    count, bins, _ = plt.hist(sample_means, bins=40, color='salmon', edgecolor='black', density=True, label='Distribuzione delle medie')
    plt.plot(bins, norm.pdf(bins, mu, sigma), 'k--', linewidth=2, label='Gaussiana teorica (TLC)')
    plt.boxplot(sample_means, vert=False, patch_artist=True,
                boxprops=dict(facecolor='lightgreen', color='black'),
                medianprops=dict(color='red', linewidth=2))
    plt.title(f"Distribuzione delle medie campionarie (n={n}, k={k})")
    plt.legend()
    plt.show()
