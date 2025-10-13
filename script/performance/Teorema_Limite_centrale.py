import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   
    n = 30 # Sample size
    k = 5000 # Numero campioni
    a = np.random.randint(1,100,10000) # Generazione della popolazione
    mean = np.array([]) # Distribuzione delle medie campionarie

    # Generazione della distribuzione campionaria
    for i in range(k):
        sample = np.random.choice(a, size=n, replace=True)
        mean = np.append(mean, np.mean(sample))
    

    plt.figure("Distribuzione originale dei dati")
    plt.hist(a, bins=30, edgecolor='black', linewidth=2, color="salmon")
    plt.title(f"Media Popolazione = {np.mean(a)}")
    plt.figure("Distribuzione delle medie campionarie")
    plt.hist(mean, bins=30, edgecolor='black', linewidth=2, color="lightgreen")
    plt.title(f"Media = {np.mean(mean)}")
    plt.show()

