fprintf('----Movimiento Unidimensional de un Globo---- \n')
fprintf('----Enrique Mondelli---- \n')

Yo = input('Posicion Inicial: '); 
Vo = input('Velocidad Inicial: ');
volumen = input('Volumen del globo: ');
M = input('Masa del globo: ');
p = 1.225;
go = 9.81;
R = 6371000;

[t, y] = ode45(@(t, y) [y(2); ((-M*(go/(1+(y(1)/R))^2) + p*volumen*(go/(1+(y(1)/R))^2)))/M], [0 5000], [Yo, Vo]);

figure(1)
plot(t, y(:,1), 'o')
title('tiempo vs posicion')


figure(2)
plot(t, y(:,2), 'o')
title('tiempo vs velocidad')


tabla = fopen('tabla.txt', 'w');
fprintf(tabla, 'tiempo      posicion      velocidad \n');
fprintf(tabla,'%2.2f       %2.2f         %2.2f \n', t, y(:,1), y(:,2));
fclose(tabla);
