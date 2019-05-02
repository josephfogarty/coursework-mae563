"""
Final Project for MAE563: Instabilities in Fluids
This code takes in a velocity time series and then produces plots of the data
and the FFT of the data, as well as calculating the Strouhal number and relating
it to the reynolds number, calculated from the inflow velocity
"""
#%% Preliminaries
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.fftpack
import os
import imageio


folder = "figs/power_spectrum"
filelist = [f for f in os.listdir(folder)]
for f in filelist:
    os.remove(os.path.join(folder, f))

d = 0.125 #diameter of cylinder
visc = 0.00078125 #viscosity of fluid
u_mean_flow_list = [0.25, 0.3125, 0.375, 0.5, 0.75, 1.0, 1.25, 1.875,\
                    2.5, 3.125, 3.75, 5.0, 6.25, 12.5, 31.25]
st_list = []
re_list = []


#%%Getting the data
for u in u_mean_flow_list:
    
    #calculate reynolds number, add to list
    re = int((u*d)/visc)
    print(f"\nCalculating for Re = {re}")
    re_list.append(re)
    
    #retrieve data , put them in arrays
    t = []
    uy = []
    
    with open(f'adroit_output/data/vvprof{re:0>4d}.dat','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            t.append(float(row[1]))
            uy.append(float(row[2]))
            
    t = np.array(t)
    uy = np.array(uy)
    
    #let's see the raw data
    plt.plot(t,uy)
    plt.xlabel('t')
    plt.ylabel('$u_y$')
    plt.title(f'$u_y$ time series, $Re$={re}')
    plt.savefig(f"figs/unedited_time_series/unedited_uy_time_series_{re:0>4d}.png")
    plt.close()
    
    #so now let's cut off the first five seconds
    #special case if Re=40 (slow flow)
    if re == 800:# or re == 800 or re == 500:
        t = t[int(-1*(len(t)/3)):]
        uy = uy[int(-1*(len(uy)/3)):]
    else:
        t = t[int(-2*(len(t)/3)):]
        uy = uy[int(-2*(len(uy)/3)):]
    
    #let's see the raw data again
    plt.plot(t,uy)
    plt.xlabel('t')
    plt.ylabel('$u_y$')
    plt.title(f'$u_y$ time series, $Re$={re}')
    plt.tight_layout()
    plt.savefig(f"figs/edited_time_series/uy_time_series_{re:0>4d}.png")
    plt.close()
    
    # Now let's look at the fft
    n = len(uy) #number of samples
    fs = len(uy)/(t[-1]-t[1]) #sampling rate, number of measurements per second
    
    #perform the fft
    uy_fft = scipy.fftpack.fft(uy) #DFT of data
    uy_psd = (np.abs(uy_fft)**2)/n #power of DFT
    freqs = scipy.fftpack.fftfreq(len(uy))*fs #frequency range
    
    plt.plot(freqs,uy_psd,"r",label=f'$f$={freqs[uy_psd.argmax()]:.4f}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (W/Hz)')
    plt.title(f'$u_y$ Power Spectrum Analysis, $Re$={re}')
    plt.xlim(-100.0,100.0)
    plt.ylim(0.0,8000.0)
    plt.legend(loc=9)
    plt.tight_layout()
    plt.savefig(f"figs/power_spectrum/uy_power_spectrum_{re:0>4d}.png")
    plt.close()
    
    #find the dominant signal
    max_uy_psd = max(uy_psd)
    max_freq = freqs[uy_psd.argmax()]
    #print(max_freq,max_uy_psd)
    
    #calculate St, add to list
    st = (max_freq*d)/u
    st_list.append(st)
    print(f"f_dom = {max_freq:.4f}\nSt = {st:.4f}")

#%% Now let's plot Re vs St vs u
fig, ax = plt.subplots()

#using empirical forumula 1
Re_x1 = np.linspace(300,2000,2500)
St_y1 = 0.198*(1-(19.7/Re_x1))
plt.plot(Re_x1,St_y1,"r",label="(Roshko, 1953)")

#using empirical formula 2
Re_x2 = np.linspace(40,1400,2000)
St_y2 = 0.1816 - (3.3265/Re_x2)
plt.plot(Re_x2,St_y2,"g",label="(Williamson, 1989)")

#using simulation data
plt.plot(re_list,st_list,"^b-",label="Simulation Data")

#put it together
plt.xscale("log")
plt.xlabel("$Re$")
plt.ylabel("$St$")
#for i, txt in enumerate(re_list):
#    ax.annotate(txt, (re_list[i], st_list[i]))
plt.title("$St$ as a function of $Re$")
plt.legend()
plt.tight_layout()
plt.savefig(f"Re_vs_St")
plt.close()

#%% Let's create some gif files of all of the figures

images = []
for file_name in os.listdir('figs/power_spectrum'):
    if file_name.endswith('.png'):
        file_path = os.path.join('figs/power_spectrum', file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave(f'figs/movie_power_spectrum.gif',images,duration=0.5)








