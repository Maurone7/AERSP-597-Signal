clear, clc, close all;
% Define the symbol 't'
syms t

% Rest of the code...
f = exp(-t);
f_matrix = subs(f, t, linspace(-4, 4, 1000))
g = exp(-2*t);
g_matrix = subs(g, t, linspace(-4, 4, 1000))

x = linspace(-4, 4, 1000);
convolution = conv(f_matrix, g_matrix);

% Plotting the functions
plot(x, convolution);

% Labeling the axes
xlabel('x');
ylabel('f(x)');
title('Convolution of f(x) and g(x)');
