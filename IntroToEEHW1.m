voltage_a = [1.600 1.500 1.450 1.435 1.425 1.415 1.395 1.385 1.375 1.365 1.345 1.320 1.310 1.305 1.300 1.285 1.275 1.215 1.200 1.165 1.150 1.100 1.050 1.000 0.985 0.9550 0.9000 0.8];
time_a = [0 25 50 75 100 125 150 175 200 225 250 275 300 325 350 375 400 425 450 475 500 525 550 575 600 625 650 675 700 725 736.55] * 3600;

p1 = -0.0047054;
p2 = -0.031508;
p3 = 0.028793;
p4 = 0.13112;
p5 = -0.039084;
p6 = -0.17991;
p7 = -0.048474;
p8 = -0.09402;
p9 = 1.2994;

z = @(x) (x-1.215e+06)/7.403e+05;
y = @(x) p1*z(x).^8 + p2*z(x).^7 + p3*z(x).^6 + p4*z(x).^5 + p5*z(x).^4 + p6*z(x).^3 + p7*z(x).^2 + p8*z(x) + p9;

% Plot both the original voltage values and the function y on the same graph
figure;
hold on;
%plot(time_a, voltage_a, 'b', 'LineWidth', 2, 'DisplayName', 'Original Voltage');
plot(time_a, arrayfun(y, time_a), 'r', 'LineWidth', 2, 'DisplayName', 'Function y');
hold off;

xlabel('Time');
ylabel('Voltage');
title('Comparison of Original Voltage and Function y');
legend('show');

% Corrected syntax for calculating the integral
integral_result = integral(y, 0, time_a(end)) * (5 * (10^-3));
disp(['Total Energy: ', num2str(integral_result), 'J']);
