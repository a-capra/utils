import numpy as np
import matplotlib.pyplot as plt

Nsample=100000
rmin=100.
rmax=190.

r = np.random.uniform(rmin, rmax, size=Nsample)
phi = np.random.uniform(0., 2.*np.pi, size=Nsample)

x = r*np.cos(phi)
y = r*np.sin(phi)
rho = np.sqrt(x**2+y**2)

plt.subplot(2,2,1)
plt.plot(x,y,'.')
plt.grid(True)
plt.subplot(2,2,3)
plt.hist(rho,bins=100)


r1 = np.random.uniform(rmin**2, rmax**2, size=Nsample)
phi1 = np.random.uniform(0., 2.*np.pi, size=Nsample)

x1 = np.sqrt(r1)*np.cos(phi)
y1 = np.sqrt(r1)*np.sin(phi)
rho1 = np.sqrt(x1**2+y1**2)

plt.subplot(2,2,2)
plt.plot(x1,y1,'.r')
plt.grid(True)
plt.subplot(2,2,4)
plt.hist(rho1,bins=100,facecolor='r')

fig=plt.gcf()
fig.set_size_inches(12.0, 12.)
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95,
                    wspace=0.15, hspace=0.15)

plt.show()
