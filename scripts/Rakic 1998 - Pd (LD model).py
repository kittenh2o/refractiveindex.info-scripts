# -*- coding: utf-8 -*-
# Original data: https://doi.org/10.1364/AO.37.005271
# Author: Mikhail Polyanskiy
# Last modified: 2017-02-22

import numpy as np
import matplotlib.pyplot as plt

# Lorentz-Drude (LD) model parameters
ωp = 9.72  #eV
f0 = 0.330
Γ0 = 0.008 #eV

f1 = 0.649
Γ1 = 2.950 #eV
ω1 = 0.336 #eV

f2 = 0.121
Γ2 = 0.555 #eV
ω2 = 0.501 #eV

f3 = 0.638
Γ3 = 4.621 #eV
ω3 = 1.659 #eV

f4 = 0.453
Γ4 = 3.236 #eV
ω4 = 5.715 #eV

Ωp = f0**.5 * ωp  #eV

def LD(ω):  #ω: eV
    ε = 1-Ωp**2/(ω*(ω+1j*Γ0))
    ε += f1*ωp**2 / ((ω1**2-ω**2)-1j*ω*Γ1)
    ε += f2*ωp**2 / ((ω2**2-ω**2)-1j*ω*Γ2)
    ε += f3*ωp**2 / ((ω3**2-ω**2)-1j*ω*Γ3)
    ε += f4*ωp**2 / ((ω4**2-ω**2)-1j*ω*Γ4)
    return ε
  
ev_min=0.1
ev_max=5
npoints=1000
eV = np.logspace(np.log10(ev_min), np.log10(ev_max), npoints)
μm = 4.13566733e-1*2.99792458/eV
ε = LD(eV)
n = (ε**.5).real
k = (ε**.5).imag

#============================   DATA OUTPUT   =================================
file = open('out.txt', 'w')
for i in range(npoints-1, -1, -1):
    file.write('\n        {:.4e} {:.4e} {:.4e}'.format(μm[i],n[i],k[i]))
file.close()
    
    
#===============================   PLOT   =====================================
plt.rc('font', family='Arial', size='14')

plt.figure(1)
plt.plot(eV, -ε.real, label="-ε1")
plt.plot(eV, ε.imag, label="ε2")
plt.xlabel('Photon energy (eV)')
plt.ylabel('ε')
plt.xscale('log')
plt.yscale('log')
plt.legend(bbox_to_anchor=(0,1.02,1,0),loc=3,ncol=2,borderaxespad=0)

#plot n,k vs eV
plt.figure(2)
plt.plot(eV, n, label="n")
plt.plot(eV, k, label="k")
plt.xlabel('Photon energy (eV)')
plt.ylabel('n, k')
plt.yscale('log')
plt.legend(bbox_to_anchor=(0,1.02,1,0),loc=3,ncol=2,borderaxespad=0)

#plot n,k vs μm
plt.figure(3)
plt.plot(μm, n, label="n")
plt.plot(μm, k, label="k")
plt.xlabel('Wavelength (μm)')
plt.ylabel('n, k')
plt.xscale('log')
plt.yscale('log')
plt.legend(bbox_to_anchor=(0,1.02,1,0),loc=3,ncol=2,borderaxespad=0)