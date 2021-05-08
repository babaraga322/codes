function optimal = dichotomous(f,a,b,n)
% Program : dichotomous.m
%
% Purpose : find the optimal point of a given single variable function 
%           within the given interval
%
% Author :  Aamir Alaud Din
% Date :    26.09.2013
%
% Inputs :  Four input arguments are required viz., function, two points
%           belonging to the interval, and number of iterations
%
% Syntax :  optimal = dichotomous(f,a,b,n)
%           where f is an inline function 
%           e.g., f = inline('sin(x)','x');
%           a and b are two points belonging to the interval
%
% Example:  optimal = dichotomous(f,-3,5,20)
if (nargin < 3)
    error('Less number of inputs');
    optimal = 'Optimal can''t be found with too few inputs';
    return;
    
elseif (nargin == 3)
    n = 250;
    disp('Iteration             a               b              f(a)            f(b)');
    disp('=========         =========       =========       =========       =========');
    for ii = 1:n
        mid = (a + b)/2;
        epsilon = 0.0001;
        a1 = mid - epsilon;
        b1 = mid + epsilon;
        if (f(a1) < f(b1))
            b = b1;
        elseif (f(a1) > f(b1))
            a = a1;
        elseif (f(a1) == f(b1))
            a = a1;
            b = b1;
        end
        fprintf('%4d', ii);
        fprintf('\t\t\t');
        fprintf('%11.4f', a);
        fprintf('\t\t');
        fprintf('%11.4f', b);
        fprintf('\t\t');
        fprintf('%11.4f', f(a));
        fprintf('\t\t');
        fprintf('%11.4f', f(b));
        fprintf('\n');
    end
    
elseif (nargin == 4)
    disp('Iteration             a               b              f(a)            f(b)');
    disp('=========         =========       =========       =========       =========');
    for ii = 1:n
        mid = (a + b)/2;
        epsilon = 0.001;
        a1 = mid - epsilon;
        b1 = mid + epsilon;
        if (f(a1) < f(b1))
            b = b1;
        elseif (f(a1) > f(b1))
            a = a1;
        elseif (f(a1) == f(b1))
            a = a1;
            b = b1;
        end
        fprintf('%4d', ii);
        fprintf('\t\t\t');
        fprintf('%11.4f', a);
        fprintf('\t\t');
        fprintf('%11.4f', b);
        fprintf('\t\t');
        fprintf('%11.4f', f(a));
        fprintf('\t\t');
        fprintf('%11.4f', f(b));
        fprintf('\n');
    end
    
elseif (nargin > 4)
    error('Too many input arguments')
    optimal = 'Optimal can''t be found with too many inputs';
    return;
end
optimal = min(a,b);