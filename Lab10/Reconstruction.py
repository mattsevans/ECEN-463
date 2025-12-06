# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 13:29:16 2025

@author: 32dir
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, fftshift, fft2

kspace = []
factors = np.linspace(1,-1, 32 ,endpoint = True)
for factor in factors:
    NFE_pts = np.loadtxt("proj0_0 (64 points) phase " + str(factor) + ".csv",delimiter=',', dtype=complex)
    k = fft(NFE_pts)
    kspace.append(k)
kspace = np.array(kspace)
plt.imshow(abs(kspace))
plt.show()
plt.imshow(np.roll(np.roll(abs(fft2(kspace)),25,1),15,0))
    
    
    
        
        