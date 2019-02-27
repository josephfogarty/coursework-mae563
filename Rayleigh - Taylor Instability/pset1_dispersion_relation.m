rho_1 = 10;
rho_2 = 12;
gamma = 0.05;
g = 20;

k_int = ((g*(rho_2 - rho_1))/gamma)^(0.5);
fprintf(num2str(k_int))
fprintf("\n")

k = 0:pi/12:8*pi;

res = real(((g.*k.*(rho_2 - rho_1)-gamma.*(k.^3))./(rho_1 + rho_2)).^(0.5));

figure;
plot(k,res)
% plot(2*pi,0,'o')
% plot(4*pi,0,'o')
% plot(8*pi,0,'o')
xmax = max(k)+5;
xlim([0 xmax])
ylim([0 15])