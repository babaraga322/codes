f = @(x) x^2 - sin(x);
a = -4;
b = 6;

epsilon = 1e-2;
t = (sqrt(5)-1)/2;

iter = 0;
while abs(b-a)>epsilon
   L = b - a;
   x1 = b - t*L;
   x2 = a + t*L;
   
   if f(x1)>f(x2)
       a = x1;
       x1 = x2;
       x2 = a + t * (b - a);
   else
       b = x2;
       x2 = x1;
       x1 = a + (1-t) * (b - a);
       
   end
       
   iter = iter + 1;
end
[a, b]
iter


