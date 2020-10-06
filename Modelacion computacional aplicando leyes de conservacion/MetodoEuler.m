function ans1 = MetodoEuler(f)
    xi = input('Valor de x inicial: ');
    xf = input('Valor de x final: ');
    n = input('Numero de pasos: ');
    h = (xf - xi)/n;
    Yo = input('Valor de y inicial: ');
    X = [xi:h:xf];

    for k=1: n+1
        y = Yo + h*f(X(k));
        Yo = y;
    end
    ans1 = y;
    fprintf('Respuesta = ')
    format shortG
    disp(num2str(ans1))
end