%% A short code to retrieve both interface and energy data from the Basilisk
% Rayleigh-Taylor solver and plot them
clear all;
clc;
clf;
cd 'D:\Coursework\MAE 563 Instabilities in Fluids\MAE563\Kelvin - Helmholtz Instability'

%% Plotting Interface Data %%%

% Import simulation results, and change the file, assuming you are
% already in MAE563/Rayleigh - Taylor Instability
interface_results = importdata('kh_vortex_sheet/pwp/results0.50_0.dat');
% [m1,n1] = size(interface_results);
% fprintf("The size of the raw data is %d by %d\n", m1, n1);

x1 = interface_results(:,1);
y1 = interface_results(:,2);

% Set Up the Figure
scatter(x1,y1,7,'filled','m');

% Add legend, axes, grid, and title
grid on
xlabel('x');
ylabel('z');
legend('t = 0.0','t = 0.1','t = 0.2','t = 0.3','t = 0.5')
title("Interfaces for KH Instability, Perturbation without Propagation");
