from getdist import plots, loadMCSamples

ednew = loadMCSamples('../results/chains/braneworld',settings={'ignore_rows':0.3})

g = plots.getSubplotPlotter()
g.plot_2d(ednew,['l','z'],filled=True)
g.export('fig2.pdf')
