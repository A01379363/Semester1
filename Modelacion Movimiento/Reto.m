v=0;
while v < 8 %ciclo while para repetir el codigo 8 veces con valores distintos
g = 9.81;%Fuerza de gravedad m/s^2
r = 10;%radio en metros
M = 0.425;%kg
angulo = 10+70*rand;%en grados
k = 0.00000768;
h0 = 1247; %metros
x0 = 0;
anguloR = deg2rad(angulo);%en radianes
V = 100 + 50*rand;%metros/segundos
V0x = V*cos(anguloR);%Calculo de valor incial de velocidad en x
V0y = V*sin(anguloR);%Calculo de valor incial de velocidad en y

%Declaracion de funciones y rutina de ode45
f1 = @(t,x) [x(2); -g-(k/M)*x(2)*sqrt(x(4)^2+x(2)^2);x(4);-(k/M)*x(4)*sqrt(x(4)^2+x(2)^2)];
[t,x] = ode45(f1, [0:0.5:200], [h0,V0y,x0,V0x]);


for a=1:length(t)*100 %Uso de ciclo for para graficar cada punto dado por ode45
        
        figure(1)
        plot(x(a,3), x(a,1), '*')
        xlabel('Posición X (m)')
        ylabel('Posición Y (m)')
        drawnow
        hold on
        %If para romper el ciclo for cuando y va por debajo de 0
        if x(a,1)<=0
            plot([((x(b,3)-x(a,3))/2)+x(a,3)-r ((x(b,3)-x(a,3))/2)+x(a,3)+r],[0,0],'LineWidth',5,'color','r')
            break
        end
       b=a; %le damos el valor a b de la a anterior para calcular con mas exactitud el punto de impacto
end
v = v+1; %Suma de variable del ciclo while
end