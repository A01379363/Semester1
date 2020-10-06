clear all

A = [-1 1 -5; -1 -3 1; 2 6 -3];
b = [-87; -73; 119];
x = A \ b
A\A 
inv(A) % returns inverse of A
mtimes(A, x) %returns values of b