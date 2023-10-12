from scipy.stats import chi2, norm
import matplotlib.pyplot as plt
import numpy as np

v_values = [1, 2, 3, 10]
k_values = [50, 100, 500, 1000]

plt.style.use("ggplot")
plt.figure(figsize=(15, 8))

location = 1
for vidx, v in enumerate(v_values):
    for kidx, k in enumerate(k_values):
        chi2_dist = np.array([])
        for i in range(k):
            samples = norm.rvs(size=v, loc=0, scale=1)
            chi2_dist = np.append(chi2_dist, (samples ** 2).sum())
        x = np.linspace(0, max(chi2_dist), 1000)
        
        plt.subplot(4, 4, location)
        plt.title(f"v={v}, k={k}")
        plt.plot(x, chi2.pdf(x, v), color='b', linewidth=2)
        plt.hist(chi2_dist, density=True)
        location += 1

plt.tight_layout()
plt.show()
