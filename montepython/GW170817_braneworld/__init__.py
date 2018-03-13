import os
from montepython.likelihood_class import Likelihood_prior
import numpy as np


class GW170817_braneworld(Likelihood_prior):

    # initialisation of the class is done within the parent Likelihood_prior. For
    # this case, it does not differ, actually, from the __init__ method in
    # Likelihood class.
    def loglkl(self, cosmo, data):

        l_mcmc = data.mcmc_parameters['l']['current']*data.mcmc_parameters['l']['scale']
        omegam_mcmc = data.mcmc_parameters['omegam']['current']*data.mcmc_parameters['omegam']['scale']
        z_mcmc = data.mcmc_parameters['z']['current']*data.mcmc_parameters['z']['scale']
        rgamma_mcmc = data.mcmc_parameters['rgamma']['current']*data.mcmc_parameters['rgamma']['scale']

        def deltat(l_dt,omegam_dt,z_dt,rgamma_dt):
            return 3.0*(l_dt**(2.0))*(omegam_dt**(2.0))*(z_dt**(4.0))/(32.0*self.c*rgamma_dt)

        loglkl = -0.5 * (deltat(l_mcmc,omegam_mcmc,z_mcmc,rgamma_mcmc) - self.deltatmeas) ** 2 / ((self.sigmadeltat ** 2)+(self.sigmaastro ** 2))
        loglkl = loglkl -0.5 * (omegam_mcmc - self.omegammeas) ** 2 / (self.sigmaomegam ** 2)
        loglkl = loglkl -0.5 * (rgamma_mcmc - self.rgammameas) ** 2 / (self.sigmargamma ** 2)
        loglkl = loglkl -0.5 * (z_mcmc - self.zmeas) ** 2 / (self.sigmaz ** 2)

        return loglkl
