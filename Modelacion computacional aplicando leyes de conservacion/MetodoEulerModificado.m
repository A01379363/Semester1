function ans1 = MetodoEulerModificado(f)
    xi = input('Valor de x inicial: ');
    xf = input('Valor de x final: ');
    Yo = input('Valor de y inicial: ');
    n = input('Numero de pasos: ');
    h = (xf - xi)/n;
    X = [xi:h:xf];
    y = [xi:h:xf];
    y(1) = Yo;
    X(1) = xi;
    
    for k=2: n+1
        yn1_a = y(k-1) + h*f(X(k-1),y(k-1));
        y(k) = y(k-1) + h*((f(X(k-1),y(k-1))+f(X(k),yn1_a))/2);
    end
    ans1 = y(n+1);
    fprintf('Respuesta = ')
    format shortG
    disp(num2str(ans1))
    disp('-----------------------------------')
    figure(1)
    title("Gráficas con Euler Modificado")
    hold on
    plot(X,y,"-o")
    hold on
    
end