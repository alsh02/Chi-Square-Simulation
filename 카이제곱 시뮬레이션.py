from scipy.stats import chi2, norm
import matplotlib.pyplot as plt
import numpy as np

v_values = [1, 2, 3, 10]
k_values = [50, 100, 500, 1000]

plt.style.use("ggplot")

for v in v_values:
    for k in k_values:
        chi2_dist = np.array([])
        for i in range(k):
            samples = norm.rvs(size=v, loc=0, scale=1)
            chi2_dist = np.append(chi2_dist, (samples ** 2).sum())
        x = np.linspace(0, max(chi2_dist), 1000)
        plt.title(f"v={v}, k={k}")
        plt.plot(x, chi2.pdf(x, v), color='b', linewidth=2)
        plt.hist(chi2_dist, density=True)
        plt.show()