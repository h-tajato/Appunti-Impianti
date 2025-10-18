import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__=="__main__":
    n = 30  # Sample size
    k = 5000  # Numero campioni
    g = 10  # Quanti campioni si vuole visualizzare (intervalli di confidenza)
    n_view = int(5000/g)

    # Popolazione
    a = np.random.randint(1, 100, 10000)
    mean = np.array([])

    sigma = np.std(a)
    alfa = 0.05
    z_alfa_2 = norm.ppf(1 - alfa / 2)
    mu_pop = np.mean(a)

    # Liste per gli intervalli da mostrare
    lower_bounds = []
    upper_bounds = []
    means = []
    sample_indices = []

    # Generazione dei campioni
    for i in range(k):
        sample = np.random.choice(a, size=n, replace=True)
        x_sample = np.mean(sample)
        mean = np.append(mean, x_sample)

        # Calcolo intervallo solo quando i % n_view == 0
        if i % n_view == 0:
            l = x_sample - ((sigma * z_alfa_2) / np.sqrt(n))
            m = x_sample + ((sigma * z_alfa_2) / np.sqrt(n))

            print(f"[Campione - {i}]\nI =[{round(l,3)},{round(m,3)}]\nmedia = {round(x_sample,3)}")

            lower_bounds.append(l)
            upper_bounds.append(m)
            means.append(x_sample)
            sample_indices.append(i)

    # -----> [DATI FINALI] <-----
    print("\n-----> [DATI FINALI] <-----")
    print(f"Media Popolazione = {round(mu_pop,3)}\nDev. Standard Popolazione = {round(sigma,3)}")
    print(f"Media della X_signed = {round(np.mean(mean),3)}\nDev. Standard della X_signed = {round(np.std(mean),3)}")

    # Conta quanti intervalli contengono la media vera
    contains_mu = np.sum((np.array(lower_bounds) <= mu_pop) & (np.array(upper_bounds) >= mu_pop))
    perc = contains_mu / len(lower_bounds) * 100
    print(f"Intervalli (mostrati) che contengono la media vera: {contains_mu}/{len(lower_bounds)} ({round(perc,2)}%)")

    # -----> [PLOT FINALE - Intervalli Verticali] <-----
    plt.figure(figsize=(8, 6))

    for i in range(len(lower_bounds)):
        color = 'green' if lower_bounds[i] <= mu_pop <= upper_bounds[i] else 'red'
        plt.plot([i, i], [lower_bounds[i], upper_bounds[i]], color=color, linewidth=2)
        plt.plot(i, means[i], 'ko', markersize=5)

    plt.axhline(mu_pop, color='blue', linestyle='--', label=f"Media Popolazione = {round(mu_pop,2)}")
    plt.title(f"Intervalli di confidenza verticali ogni {n_view} campioni (n={n})\n{round(perc,1)}% contengono μ")
    plt.xlabel("Campione (ogni n_view)")
    plt.ylabel("Valore")
    plt.legend()
    plt.tight_layout()
    plt.show()
