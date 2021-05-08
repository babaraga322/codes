clc;
clear all;

f = @(x)  exp(x) - 2*x + 0.01/x - 0.000001/(x^2);
epsilon = 1e-6;
a = 0.5449;
b =  0.7674;
syms x
d_f=diff(f,x);
f1 = double(vpa(subs(d_f,x,a)));
f2 = double(vpa(subs(d_f,x,b)));

x1 = a+(f1+(3*((f(a)-f(b))/(b-a))+f1+f2)+(((3*((f(a)-f(b))/(b-a))+f1+f2)^2-f1*f2)^.5))*(b-a)/(2*(3*((f(a)-f(b))/(b-a))+f1+f2)+f1+f2);
x2 = a+(f1+(3*((f(a)-f(b))/(b-a))+f1+f2)-(((3*((f(a)-f(b))/(b-a))+f1+f2)^2-f1*f2)^.5))*(b-a)/(2*(3*((f(a)-f(b))/(b-a))+f1+f2)+f1+f2);
x3 = max(x1,x2);
n=double(vpa(subs(d_f,x,x3)));
iter = 1;
while abs(n)>epsilon
    
    f1 = double(vpa(subs(d_f,x,a)));
    f2 = double(vpa(subs(d_f,x,b)));
    x1=a+(f1+(3*((f(a)-f(b))/(b-a))+f1+f2)+(((3*((f(a)-f(b))/(b-a))+f1+f2)^2-f1*f2)^.5))*(b-a)/(2*(3*((f(a)-f(b))/(b-a))+f1+f2)+f1+f2);
    x2=a+(f1+(3*((f(a)-f(b))/(b-a))+f1+f2)-(((3*((f(a)-f(b))/(b-a))+f1+f2)^2-f1*f2)^.5))*(b-a)/(2*(3*((f(a)-f(b))/(b-a))+f1+f2)+f1+f2);
    x3=max(x1,x2);
    n=double(vpa(subs(d_f,x,x3)));
    if n<0
        a = x3;
    elseif n>0
        b = x3;
    end
    iter = iter + 1
end
iter
x3
f(x3)
