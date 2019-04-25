#%%Instabilities PSet 2
#Taking interfaces code from MATLAB and using it here
#A short code to retrieve and plot interface data
#Created on Fri Apr 12 11:03:38 2019
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
#%% Plotting Interface Data %%%

folder = "figures/giffiles"
filelist = [f for f in os.listdir(folder)]
for f in filelist:
    os.remove(os.path.join(folder, f))

# get correct file name
perturb = '025';

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
    
    for j in range(0,4):
        data_loc_string = f'Level11Re300000eps{perturb}/Interface/results{num}{str(j)}.dat'
        
        #print(data_loc_string)
        interface_results = np.loadtxt(data_loc_string, delimiter=' ',dtype=float)
        x1 = interface_results[:,0]
        y1 = interface_results[:,1]
        
        #Plot Figure
        plt.scatter(x1, y1, s=1, color='b');
    
    #Save plot for movie
    plt.title("Interfaces for B-F Instability");
    plt.xlabel("x")
    plt.ylabel("z")
    plt.savefig("figures/giffiles/plot"+filetitle+".png")
    plt.close()

# Moive Time
png_dir = 'figures/giffiles/'
images = []
for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave(f'figures/bfmovie{perturb}.gif',images)

