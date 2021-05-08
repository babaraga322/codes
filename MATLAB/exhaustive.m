f = @(x) x^2 - sin(x);
a = -4;
b = 6;


n = 1e3;
delta = (b - a)/n;

x1 = a;
x2 = x1 + delta;
x3 = x2 + delta;

while true
    
   iter = iter + 1;
   
   if f(x1)>=f(x2)
       if f(x3)>f(x2)
          break 
       end
   end
   
   ;
   x1 = x2;
   x2 = x3;
   x3 = x2 + delta;
end
[x1 x3]
iter