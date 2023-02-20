import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')
rc('font', size=11)

plt.close('all') # tidy up any unshown plots

x = np.linspace(0,10,128)
xdata = x[::10]

plt.figure(1, figsize=(4.5, 3.75))
plt.subplot(111)
plt.plot(x, x, 'c-', label='$\mathrm{Linear \, fit} \, x$') # LaTeX mathmode with \mathrm{} for text and \, for spaces
plt.plot(x, x**2., 'm-', label='$\mathrm{Quadratic \, fit} \, x^{2}$')
plt.plot(xdata, (xdata + xdata**2.)/2., 'ko', label='$\mathrm{Data}$')
plt.xlabel('$x \, [\mathrm{kms}^{-1}]$')
plt.ylabel('$\Psi \, [\mathrm{arb.}]$')
plt.legend(frameon=False, fontsize='small', loc='upper left', numpoints=1)
plt.savefig('linear_square.png', bbox_inches='tight', dpi=320)

plt.figure(2, figsize=(9, 3.75))
plt.subplot(121)
plt.imshow(np.random.normal(size=[128,128]), interpolation='nearest', cmap='plasma', origin='lower', extent=(-5,5,-5,5))
plt.xlabel('$x \, \mathrm{[arcsec]}$')
plt.ylabel('$y \, \mathrm{[arcsec]}$')
plt.title('$\mathrm{Gaussian}$')
plt.subplot(122)
plt.imshow(np.random.poisson(size=[128,128]), interpolation='nearest', cmap='plasma', origin='lower', extent=(-5,5,-5,5))
plt.xlabel('$x \, \mathrm{[arcsec]}$')
plt.ylabel('$y \, \mathrm{[arcsec]}$')
plt.title('$\mathrm{Poisson}$')
plt.savefig('random_noise.png', bbox_inches='tight', dpi=320)