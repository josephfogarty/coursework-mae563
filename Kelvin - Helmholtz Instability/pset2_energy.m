%% A short code to retrieve both interface and energy data from the Basilisk
% Kelvin-Helmholtz solver and plot them
clear all;
clc;
clf;

%% Plotting Energy %%

% Import simulation results
energy_results = importdata('kh_vortex_sheet/u2_gt_vc/new/budgetFluid1.dat');
energy_results = energy_results.data(2:end,1:2);
%[m1,n1] = size(energy_results);
%fprintf("The size of the raw data is %d by %d\n", m1, n1);

% Create two vectors to be plotted
x2 = energy_results(:,1);
y2 = energy_results(:,2);

% Now plot energy
scatter(x2,y2,7,'filled','k')
% plot(x,y)
ylabel('Energy (E)');
xlabel('time (t)');
titlestr = sprintf("Energy for 0.02 thickness BL");
title(titlestr);
grid on

% Optional include legend
%legend('\gamma = 0.1, g = 10','\gamma = 0.05, g = 10','\gamma = 0.05, g = 12')

%% Growth Rate
xgrowth=x2(1:161);
ygrowth=y2(1:161);