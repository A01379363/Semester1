clear all;

span = [1,1.5];

f1 = @(X,y) 2*X*y;
MetodoEulerModificado(f1);
[x1,y1] = ode45(f1,span,1);

f2 = @(X,y) 2*X - 3*y + 1;
MetodoEulerModificado(f2);
[x2,y2] = ode45(f2,span,1);

f3 = @(X,y) X*y.^2 - y/X;
MetodoEulerModificado(f3);
[x3,y3] = ode45(f3,span,1);

figure(2)
title('Gráficas con ODE45')
hold on
plot(x1,y1,"-o");
hold on
plot(x2,y2,"-o");
hold on
plot(x3,y3,"-o");