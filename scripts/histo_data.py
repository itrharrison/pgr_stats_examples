import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')
rc('font', size=11)

plt.close('all') # tidy up any unshown plots

mu = 5.0
sigma = 10.0

npoints = int(1e5)
nbins = 30

r_data = np.random.normal(mu, sigma, size=npoints)
r_data_underdisp = np.random.normal(mu, 0.5 * sigma, size=npoints)
r_data_smallsample = np.random.normal(mu, sigma, size=npoints // 2)

r_theory = np.linspace(-45, 45, 1024)
dens_theory = stats.norm.pdf(r_theory, loc=mu, scale=sigma)

plt.figure(1, figsize=(4.5, 3.75))
plt.hist(r_data, bins=np.linspace(r_data.min(), r_data.max(), nbins), label='Data')
plt.xlabel('$r$')
plt.ylabel('Count')
plt.xlim([-40+5, 40+5])
plt.savefig('plots/1d_data.png', bbox_inches='tight', dpi=300)

plt.figure(2, figsize=(4.5, 3.75))
plt.hist(r_data,
         density=True,
         bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data')
plt.plot(r_theory, dens_theory, '-', label='Model')
plt.xlabel('$r$')
plt.ylabel('Density')
plt.xlim([-40+5, 40+5])
plt.legend()
plt.savefig('plots/1d_data_density.png', bbox_inches='tight', dpi=300)

plt.figure(3, figsize=(4.5, 3.75))
plt.hist(r_data, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data', histtype='step')
plt.hist(r_data_underdisp, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data (lower sigma)', histtype='step')
plt.hist(r_data_smallsample, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data (fewer samples)', histtype='step')
plt.xlabel('$r$')
plt.ylabel('Count')
plt.xlim([-40+5, 40+5])
plt.legend(fontsize='x-small', loc='upper left')
plt.savefig('plots/1d_data_step.png', bbox_inches='tight', dpi=300)

plt.figure(4, figsize=(4.5, 3.75))
plt.hist(r_data, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data', histtype='step', density=True)
plt.hist(r_data_underdisp, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data (lower sigma)', histtype='step', density=True)
plt.hist(r_data_smallsample, bins=np.linspace(r_data.min(), r_data.max(), nbins),
         label='Data (fewer samples)', histtype='step', density=True)
plt.xlabel('$r$')
plt.ylabel('Density')
plt.xlim([-40+5, 40+5])
plt.legend(fontsize='x-small', loc='upper left')
plt.savefig('plots/1d_data_step_density.png', bbox_inches='tight', dpi=300)