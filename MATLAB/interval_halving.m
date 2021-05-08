f = @(x) x^2 - sin(x);
a = -4;
b = 6;

epsilon = 1e-4;

iter = 0;

while abs(b-a)>epsilon
    
    x0 = (a+b) / 2;
    x1 = (a+x0)/2;
    x2 = (b+x0)/2;
    if f(x2)>f(x0) && f(x1)<f(x0)
        b = x0;
    elseif f(x2)<f(x0) && f(x1)>f(x0)
        a = x0;     
    elseif f(x2)>f(x0) && f(x1)>f(x0)
        a = x1;
        b = x2;
        
    end 
    iter = iter + 1;
end
[x1,x2]
iter