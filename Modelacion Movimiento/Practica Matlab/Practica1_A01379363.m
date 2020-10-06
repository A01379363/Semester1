fprintf('-------Oscilador armónico simple y amortiguado------- \n');
%Enrique Alberto Mondelli Romero
M = input('Cual es la masa de la particula? ');
A = input('Cual es la amplitud del movimiento en metros? ');
k = input('Cual es la constante de restitucion? ');
theta = 0;
Xo = A;
w = (k/M)^(1/2);
Vo = 0;

fprintf('La frecuencia angular es (en rad/s):');
disp(round(w,2));

x = @(t) A*cos(w*t+theta);
deriv_x = @(t) -A*w*sin(w*t+theta);
second_deriv_x = @(t) -A*w^2*cos(w*t+theta);
t = [0:0.1:10];
varx = x(t);
varx_deriv = deriv_x(t);
varx_second_deriv = second_deriv_x(t);


tabla = fopen('tabla.txt', 'w');
fprintf(tabla, "x(t)      v(t)\n");
fprintf(tabla,'%2.2f      %2.2f\n',varx,varx_deriv);
fclose(tabla);

figure(1)
plot(t,x(t))
title('Grafica Y vs t')
hold on
plot(t,deriv_x(t))
legend('x(t)','v(t)')


tspan = [0 10];
[t2,x2] = ode45(@(t2,x2) [x2(2);-k*x2(1)/M], tspan, [A,Vo]);

figure(2)
plot(t2, x2, '-o')
legend('x(t)', 'v(t)')

tabla2 = fopen('tabla2.txt', 'w');
fprintf(tabla2, "x(t)      v(t)\n");
fprintf(tabla2,'%2.2f      %2.2f\n',x2(:,1),x2(:,2));
fclose(tabla2);

B1 = 2*M*w;
[t3,x3] = ode45(@(t3,x3) [x3(2);(-k*x3(1)-B1*x3(2))/M], [1 100], [A,Vo]);

B2 = 2*M*w + 1;
[t4,x4] = ode45(@(t4,x4) [x4(2);(-k*x4(1)-B2*x4(2))/M], [1 100], [A,Vo]);

B3 = 2*M*w - 1;
[t5,x5] = ode45(@(t5,x5) [x5(2);(-k*x5(1)-B3*x5(2))/M], [1 100], [A,Vo]);

figure(3)
plot(t3, x3(:,1),'ob',t4,x4(:,1),'og',t5,x5(:,1),'or')
legend('B = 2Mw', 'B > 2Mw', 'B<2Mw')


