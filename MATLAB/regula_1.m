clc
clear
func = @(x) (668.06/x)*(1 - exp(-0.146843*x)) - 40;

epsilon = 1e-4;
x_low = 12;
x_up = 16;
table = [];
count = 0;
tic
while true
    count = count + 1;
    x_new = (func(x_up)*x_low - func(x_low)*x_up)/(func(x_up) - func(x_low));
    table = [table; x_low, x_up, x_new]
    if round(func(x_new),4)==0 || abs(x_up - x_low)<epsilon
        x_new
        break
    else
        if func(x_low)*func(x_new)<0
            x_up = x_new;
        else
            x_low = x_new;
        end
    end
    
end
toc
T = array2table(table);
T.Properties.VariableNames = {'x_low' 'x_up','x_new'};
