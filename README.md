# Braneworld-extra-dimensions

This repository contains a set of results and tools to reproduce the results from:

L. Visinelli, N. Bolis, S. Vagnozzi, [Brane-world extra dimensions in light of GW170817](https://inspirehep.net/record/1636969), [arXiv: 1711.06628](https://arxiv.org/abs/1711.06628) (VBV17)

where constraints on the size of the AdS<sub>5</sub> radius of curvature within the [Randall-Sundrum brane-world model](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.4690) are placed in light of the near-simultaneous detection of the gravitational wave event GW170817 and its optical counterpart, the short γ-ray burst event GRB170817A ([Astrophys.J. 848 (2017) no.2, L13](http://iopscience.iop.org/article/10.3847/2041-8213/aa920c/meta)). The content of the folders is described below.

## montepython

This folder contains a patch to the [Montepython](https://github.com/baudren/montepython_public) cosmological MCMC sampler to sample the posterior distribution of the 4-dimensional parameter space in VBV17 and obtain constraints on the parameters.

The *[GW170817_braneworld/](https://github.com/sunnyvagnozzi/Braneworld-extra-dimensions/tree/master/montepython/GW170817_braneworld)* folder implements the likelihood (Eq.(19) in VBV17), hence the name of the experiment you want to use in your run is "GW170817_braneworld" as per Montepython's philosophy. You should copy this folder into your montepython/montepython/likelihoods folder. You should also copy the contents of the *[covmat/](https://github.com/sunnyvagnozzi/Braneworld-extra-dimensions/tree/master/montepython/covmat)* folder into your montepython/covmat folder (assuming you want to supply an input covariance matrix to your runs, which is recommended).

The input .param file to do the MCMC run is *braneworld.param*. To run the MCMC you then want to do something like (customize your arguments as you prefer, see [Montepython's documentation](http://monte-python.readthedocs.io/en/latest/)): 

    $ python montepython/MontePython.py run -p braneworld.param -o chains/braneworld -N 100000 --chain-num 1 --update 300 -c covmat/braneworld.covmat [optional arguments]

The supplied *braneworld.sl* file is a batch file which can be used to run the MCMC on the NERSC supercomputer [Cori](http://www.nersc.gov/users/computational-systems/cori/). To submit, type:

    $ sbatch braneworld.sl

The script runs 8 chains in parallel on 1 node, using 4 cores/chain (Cori has 32 cores per node) for 40 minutes (which is more than enough to get a convergence R-1 way better than 0.01. If you want to run on the NERSC supercomputer [Edison](http://www.nersc.gov/users/computational-systems/edison/) I recommend instead running 6 chains (i.e. change "-n 8" to "-n 6" in braneworld.sl). You can also use hyperthreading but you don't gain much in terms of running time.
