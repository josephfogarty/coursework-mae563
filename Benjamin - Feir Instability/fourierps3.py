# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 20:41:36 2019

@author: jf38
"""

#%%Instabilities PSet 2
#Taking interfaces code from MATLAB and using it here
#A short code to retrieve and plot interface data
#Created on Fri Apr 12 11:03:38 2019
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio

#%% Getting Interface FFT Data %%%

folder = "figures/fftfiles"
filelist = [f for f in os.listdir(folder)]
for f in filelist:
    os.remove(os.path.join(folder, f))

# get correct file name
perturb = '02';

for i in range(0,41):

    # Set file title
#    if i%2 == 0:
#        ii = int(i/2)
#    else:
#        ii = i/2
#        print(f"i={i}")
#    print(f"ii={ii}")

    filetitle = f"time{i}s"
    num = f"{i}.00_"
    
    x1 = []
    y1 = []
    
    for j in range(0,4):
        data_loc_string = f'Level11Re300000eps{perturb}/Interface/results{num}{str(j)}.dat'
        
        #print(data_loc_string)
        interface_results = np.loadtxt(data_loc_string, delimiter=' ',dtype=float)
        x1.extend(interface_results[:,0])
        y1.extend(interface_results[:,1])
        
    yf = np.fft.fft(y1)
    
    plt.ylim((-4,4))
    #plt.xlim(())
    plt.scatter(x1, yf, s=1, color='b');
    
    #Save plot for movie
    plt.title(f"Interfaces for B-F Instability, t={i}");
    plt.xlabel("x")
    plt.ylabel("z")
    plt.savefig("figures/fftfiles/plot"+filetitle+".png")
    plt.close()

# Moive Time
png_dir = 'figures/fftfiles/'
images = []
for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave(f'figures/fftmovie{perturb}.gif',images)

