g = 9.81;
l = 1;
Xo = 0;
Vo = 2;
Vo2 = 7;
a = 0.5;
Fo = 5;
k = 0.23;
M = 1;
w = (k/M)^(1/2);
y1 = .8;
y2 = 1.2;
y3 = (k/M)^(1/2);

[t, x] = ode45(@(t, x) [x(2); (-g/l)*sin(x(1))], [0 10], [Xo, Vo]);
[t2, x2] = ode45(@(t2, x2) [x2(2); (-g/l)*sin(x2(1))], [0 10], [Xo, Vo2]);

figure(1)
plot(t, x(:,1))
hold on
plot(t2, x2(:,1))
legend('Vo = 2', 'Vo = 7')


[t3, x3] = ode45(@(t3, x3) [x3(2); (-g/l)*sin(x3(1))-a*x3(2)], [0 10], [Xo, Vo]);
[t4, x4] = ode45(@(t4, x4) [x4(2); (-g/l)*sin(x4(1))-a*x4(2)], [0 10], [Xo, Vo2]);

figure(2)
plot(x3(:,2), x3(:,1))
hold on
plot(x4(:,2), x4(:,1))
legend('Vo = 2', 'Vo = 7')


[t5, x5] = ode45(@(t5, x5) [x5(2); (-k*x5(1) + (Fo*sin(y1*t5)))/M], [0:0.1:100], [Xo, Vo]);
[t6, x6] = ode45(@(t6, x6) [x6(2); (-k*x6(1) + (Fo*sin(y1*t6)))/M], [0:0.1:100], [Xo, Vo2]);

figure(3)
plot(t5, x5(:,1))
hold on
plot(t6, x6(:,1))
legend('Vo = 2', 'Vo = 7')

[t7, x7] = ode45(@(t7, x7) [x7(2); (-k*x7(1) + (Fo*sin(y2*t7)))/M], [0:0.1:100], [Xo, Vo]);
[t8, x8] = ode45(@(t8, x8) [x8(2); (-k*x8(1) + (Fo*sin(y2*t8)))/M], [0:0.1:100], [Xo, Vo2]);

figure(4)
plot(t7, x7(:,1))
hold on
plot(t8, x8(:,1))
legend('Vo = 2', 'Vo = 7')

[t9, x9] = ode45(@(t9, x9) [x9(2); (-k*x9(1) + (Fo*sin(y3*t9)))/M], [0:0.1:100], [Xo, Vo]);
[t10, x10] = ode45(@(t10, x10) [x10(2); (-k*x10(1) + (Fo*sin(y3*t10)))/M], [0:0.1:100], [Xo, Vo2]);

figure(5)
plot(t9, x9(:,1))
hold on
plot(t10, x10(:,1))
legend('Vo = 2', 'Vo = 7')
