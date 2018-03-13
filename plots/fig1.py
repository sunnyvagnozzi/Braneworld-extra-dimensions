import getdist.plots, os
g=getdist.plots.GetDistPlotter(plot_data='../results/plot_data/')
g.settings.setWithSubplotSize(3.0000)
g.settings.prob_label = r'$P/P_{\rm max}$'
labels = [r'Posterior of $\ell$ (Mpc)']
outdir='./'
roots=['braneworld']
params=['l']
g.plots_1d(roots, params, legend_labels=[], colors='blue')
g.add_legend(labels, legend_loc='upper right', align_right=True,fontsize=5)
g.export(os.path.join(outdir,'fig1.pdf'))
