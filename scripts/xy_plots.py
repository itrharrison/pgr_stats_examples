import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')
rc('font', size=11)

plt.close('all') # tidy up any unshown plots

def model(x, m=20., c=-30., n=2):

    y = m * np.power(x, n) + c

    return y

obs_bias = 0.0
obs_scatter = 100.

x_theory = np.linspace(0, 11, 1024)
x_data = np.linspace(1, 10, 10)

y_theory = model(x_theory)
y_data = model(x_data) + np.random.normal(obs_bias, obs_scatter, size=len(x_data))
dy_data = obs_scatter * np.ones_like(y_data)


plt.figure(1, figsize=(4.5, 3.75))
plt.plot(x_theory, y_theory, '-', label='Model', zorder=-1, c='C0')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.xlim([0, 11])
plt.ylim([-100, 2100])
plt.axhline(0., c='k', alpha=0.4, linestyle='dashed')
plt.savefig('plots/model.png', bbox_inches='tight', dpi=300)

plt.figure(2, figsize=(4.5, 3.75))
plt.plot(x_data, y_data, 'o', ms=3, c='C1', label='Data')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.xlim([0, 11])
plt.ylim([-100, 2100])
plt.axhline(0., c='k', alpha=0.4, linestyle='dashed')
plt.savefig('plots/data_noerr.png', bbox_inches='tight', dpi=300)

plt.errorbar(x_data, y_data, yerr=dy_data, fmt='none', c='C1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.savefig('plots/data.png', bbox_inches='tight', dpi=300)

plt.figure(1, figsize=(4.5, 3.75))
plt.plot(x_data, y_data, 'o', ms=3, c='C1', label='Data')
plt.errorbar(x_data, y_data, yerr=dy_data, fmt='none', c='C1')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.savefig('plots/model_data.png', bbox_inches='tight', dpi=300)
