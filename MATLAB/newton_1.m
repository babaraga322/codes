clc
clear
func = @(x) (668.06/x)*(1 - exp(-0.146843*x)) - 40;
d_func = @(x) (4904996729 * exp(-0.146843*x) / (50000000 * x)) - 33403*(1 - exp(-0.146843*x))/(50*x^2);

epsilon = 1e-4;
x_start = 16;
table = [];
count = 0;

tic
while true
    count = count + 1;
    
    x_new = x_start - (func(x_start)/d_func(x_start));
    table = [table; x_start, x_new];
    if abs(x_new - x_start)<epsilon
        x_new
        break
    else
        x_start = x_new;
    end
end
toc
T = array2table(table);
T.Properties.VariableNames = {'x_start' 'x_new'};

