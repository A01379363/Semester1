#include <math.h>
#include <iostream>

using namespace std;

float ecuacion_1(float x)
{
    float x_rad = 0;
    x_rad = M_PI * x / 180;
    return pow(sin(1/x_rad), 2) / x;
}

int main(void)
{
    float numero = 0;
    cout << "Dame un numero: " << endl;
    cin >> numero;
    cout << "El resultado es: " << ecuacion_1(numero) <<endl;
}
