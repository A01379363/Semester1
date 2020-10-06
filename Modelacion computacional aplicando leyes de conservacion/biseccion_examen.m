f = @(x) 2.^(-x)-x;
biseccion(f, 0, 1);

f = @(x) 1+3*exp(-x)-x.^4;
biseccion(f, 0, 2);
