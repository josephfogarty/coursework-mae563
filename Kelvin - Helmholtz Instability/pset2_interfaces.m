%% A short code to retrieve both interface and energy data from the Basilisk
% Rayleigh-Taylor solver and plot them
clear all;
clc;
clf;

%% Plotting Interface Data %%%

% Import simulation results, and change the file, assuming you are
% already in MAE563/Rayleigh - Taylor Instability
interface_results = importdata('kh_vortex_sheet/u2_gt_vc/results0.20_0.dat');
% [m1,n1] = size(interface_results);
% fprintf("The size of the raw data is %d by %d\n", m1, n1);

x1 = interface_results(:,1);
y1 = interface_results(:,2);

% Set Up the Figure
scatter(x1,y1,7,'filled','k');

% Add legend, axes, grid, and title
grid on
xlabel('x');
ylabel('z');
%legend('t = 0.0','t = 0.2','t = 0.4','t = 0.8')%,'t = 2.0')
title("Interfaces for KH Instability, above V_c");
