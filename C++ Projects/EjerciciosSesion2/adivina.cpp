#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(void)
{
    int intentos = 5;
    int ans = 0;
    srand(time(0));
    ans = rand() % 10 + 1; //assigna un numero random del 1 al 10
    for(int indice = 0; indice < 5; indice++) //
    {
        cout <<"Tienes " << intentos - indice <<" intentos" << endl;
        int intento = 0;
        cout <<"Adivina un número entre 0 y 10: " << endl;
        cin >> intento;
        if (intento == ans)
        {
            cout <<"Adivinaste!" << endl;
            break;
        }
        else
        {
            cout <<"Fallaste" << endl;
            if (intento < ans)
            {
                cout <<"El número que elegiste es menor al que buscas..." << endl;
            }
            else
            {
                cout <<"El número que elegiste es mayor al que buscas..." << endl;
            }
        }
    }
}
