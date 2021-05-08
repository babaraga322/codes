clc
clear

func = @(x) -0.5*x^2 +2.5*x +4.5;

epsilon = 1e-4;
x_low = 5;
x_up = 10;

count=0;
table = [];
tic
while abs(x_up - x_low)>epsilon
    count = count + 1;
    midpoint = (x_low + x_up)/2;
    table = [table; x_low, x_up, midpoint];
    if func(midpoint)==0
        
        break
    else
        if func(x_low)*func(midpoint)<0
            x_up = midpoint;
        else
            x_low = midpoint;
        end     
    end
end
midpoint
toc
T = array2table(table);
T.Properties.VariableNames = {'x_low' 'x_up' 'x_mid'};