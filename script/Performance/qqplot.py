import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t, uniform, skewnorm

np.random.seed(42)

def qq_plot(data, title):
    """Disegna Q-Q plot e istogramma con curva normale tratteggiata"""
    data_sorted = np.sort(data)
    n = len(data_sorted)
    probs = (np.arange(1, n + 1) - 0.5) / n
    theoretical_quantiles = norm.ppf(probs)

    # Grafico combinato
    plt.figure(figsize=(10, 4))

    # --- Q-Q Plot ---
    plt.subplot(1, 2, 1)
    plt.scatter(theoretical_quantiles, data_sorted, color='steelblue', s=30)
    plt.plot(theoretical_quantiles, theoretical_quantiles, color='red', linestyle='--', label='Linea ideale')
    plt.xlabel("Quantili teorici (Normale standard)")
    plt.ylabel("Quantili campionari")
    plt.title(f"Q–Q Plot — {title}")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # --- Istogramma ---
    plt.subplot(1, 2, 2)
    plt.hist(data, bins=30, density=True, edgecolor='black', linewidth=1.2, color='lightgray', alpha=0.8)

    # Curva normale teorica (stessa media e varianza dei dati)
    mu, sigma = np.mean(data), np.std(data)
    x = np.linspace(min(data), max(data), 200)
    y = norm.pdf(x, mu, sigma)
    plt.plot(x, y, 'r--', label=f'Normale teorica\nμ={mu:.2f}, σ={sigma:.2f}')

    plt.title(f"Istogramma — {title}")
    plt.xlabel("Valori")
    plt.ylabel("Densità")
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


# Distribuzione normale
data_normal = np.random.normal(0, 1, 200)
qq_plot(data_normal, "(a) Normal")

# Long tails — code pesanti (Student t)
data_long_tails = t(df=2).rvs(200)
qq_plot(data_long_tails, "(b) Long tails")

# Short tails — code corte (Uniforme)
data_short_tails = uniform(-2, 4).rvs(200)
qq_plot(data_short_tails, "(c) Short tails")

# Asymmetric — distribuzione asimmetrica (Skew Normale)
data_asymmetric = skewnorm(a=5, loc=0, scale=1).rvs(200)
qq_plot(data_asymmetric, "(d) Asymmetric")
