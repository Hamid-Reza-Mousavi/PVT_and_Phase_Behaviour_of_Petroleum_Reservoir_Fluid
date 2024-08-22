clc;
clear all;

% +++++++++++++++++ Inputs +++++++++++++++++
split = 45;  % Must be greater than 7
Z_plus_fraction = 3.92;
Md = 165;
tau = 90;
gamma = 2;
Beta = (Md - tau) / gamma;
Mn = [90, 101.5, 114, 127.5, 140.5, 154, 168, 182.5, 198, 214, 229.5, 244, 257, 269, 283, 295.5, 306, 318, 330.5, 343, 354.5, 366, 377, 388, 399, 409.5, 420.5, 431.5, 441, 450.5, 460, 469.5, 479.5, 489.5, 498.5, 507, 516.5, 526, 535, 544]';
% +++++++++++++++++++++++++++++++++++++++++++

fprintf('==========================\n');
fprintf('Split: %f\n', split);
fprintf('Md: %f\n', Md);
fprintf('tau: %f\n', tau);
fprintf('gamma: %f\n', gamma);
fprintf('Beta: %f\n', Beta);
fprintf('==========================\n');

% ========= Plot Gamma probability function =========
F = zeros(length(Mn), 1);
for i=1:length(Mn)
    F(i) = F_cal(Mn(i), tau, gamma, Beta);
end

plot(Mn(2:39), F(2:39), 'o-');
title('Gamma probability function');
ylabel('F(M)');
xlabel('Molecular Weight');

% ========= Calculate the area under the curve =========

Zcn_normlized = zeros(split-7+1, 1);
for i = 1:(split-7+1)
    Mn_plus = Mn(i+1);
    Mn_minus = Mn(i);
    % Calculate the area under the curve using trapz
    area = trapz([Mn_minus, Mn_plus], [F_cal(Mn_minus, tau, gamma, Beta), F_cal(Mn_plus, tau, gamma, Beta)]);
    Zcn_normlized(i) = area;
end

% ================= 3 conditions =======================

if sum(Zcn_normlized) == 1
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
    disp('sum Zcn_normlized is 1.')
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
elseif sum(Zcn_normlized) > 1
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
    disp('sum Zcn_normlized grater than 1 >>>>>> Normlizing the ZCn.')
    Zcn_normlized = Zcn_normlized ./ sum(Zcn_normlized);
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
else
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
    disp('sum Zcn_normlized is less than 1 >>>>>> Adjuste last component.')
    Zcn_normlized(end) = Zcn_normlized(end) + (1 - sum(Zcn_normlized));
    fprintf('Sum Zcn_normlized: %f\n', sum(Zcn_normlized));
end

% ============== Show result in Table ===================

fprintf('==========================\n');
Zcn = Z_plus_fraction * Zcn_normlized;
fprintf('Sum Zcn: %f\n', sum(Zcn));
% Create empty arrays to store the table data
C = [];
Zcn_values = [];
Zcn_normalized_values = [];


% Populate the arrays with the data
for i = 1:(split - 7 + 1)
    C = [C; i + 6];
    Zcn_values = [Zcn_values; Zcn(i)];
    Zcn_normalized_values = [Zcn_normalized_values; Zcn_normlized(i)];
end

% Create the table using the arrays
T = table(C, Zcn_values, Zcn_normalized_values, 'VariableNames', {'C', 'Zcn', 'Zcn_normalized'});

% Display the table
disp(T);

