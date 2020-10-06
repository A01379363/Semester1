function ans1 = biseccion(f, a, b)
    n = 0;
    while n == 0
        fa = f(a);
        fb = f(b);
        p = (b+a)/2;
        fp = f(p);
        if (fp == 0)
            ans1 = p;
            disp(num2str(ans1))
            n = 1;
        else
            if ((fp < 0 && fa < 0) || (fp > 0 && fa > 0))
            a = p;
            elseif ((fp < 0 && fb < 0) || (fp > 0 && fb > 0))
                b = p;
            end 
        end 
    end
end