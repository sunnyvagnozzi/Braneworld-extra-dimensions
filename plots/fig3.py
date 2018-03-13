import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()
column_labels = [r'$\ell$',r'$\Omega_m$',r'$z$',r'$r_{\gamma}$',r'$\delta t$']
row_labels = [r'$\ell$',r'$\Omega_m$',r'$z$',r'$r_{\gamma}$',r'$\delta t$']
correlation = np.loadtxt('../results/braneworld.corr')
heatmap = ax.pcolor(correlation,cmap=plt.cm.Blues_r)
ax.set_xticks(np.arange(correlation.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(correlation.shape[1])+0.5, minor=False)
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
fig.colorbar(heatmap)
plt.savefig('fig3.pdf')
