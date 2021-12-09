import numpy as np
import matplotlib.pyplot as plt

lp = np.loadtxt("lp_2_3.txt")
lpcc = np.loadtxt("lpcc_2_3.txt")
mfcc = np.loadtxt("mfcc_2_3.txt")

fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle("Coeficientes 2 y 3 de las tres parametrizaciones: LP, LPCC y MFCC", weight='bold')

axs[0].scatter(lp[:, 0], lp[:, 1], label="LP", c='red', s=0.5)
axs[1].scatter(lpcc[:, 0], lpcc[:, 1], label="LPCC", c='green',  s=0.5)
axs[2].scatter(mfcc[:, 0], mfcc[:, 1], label="MFCC", c='blue', s=0.5)

for i in range(3):
    axs[i].set_ylabel("Coeficiente 3")
    axs[i].set_xlabel("Coeficiente 2")
    axs[i].legend()

plt.tight_layout()
plt.show()

