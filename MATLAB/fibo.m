f = @(x)  exp(x) - 2*x + 0.01/x - 0.000001/(x^2);
a = 0.1;
b = 10;
L0 = b - a;

i = 2;
n = 10;
iter = 0;

while i<n
    Lk = fibonacci(n-i+1)/(fibonacci(n+1))*L0;
    x1 = a + Lk;
    x2 = b - Lk;
    
    
    if f(x1)>f(x2)
        a = x1;
        x1 = x2;
    else
        b = x2;
        x2 = x1;
    end
    
    i = i + 1;
    iter = iter + 1;
end
[a, b, (a+b)/2]
iter