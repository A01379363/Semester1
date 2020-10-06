#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;


int main(void)
{
    int terminos = 0;
    cout <<"Cuántos numeros quieres que tenga la lista: " << endl;
    cin >> terminos;
    int numeros[terminos];
    srand(time(0));
    for(int id = 0; id < terminos; id++)
    {
        int num = 0;
        num = rand() % 20 + 1;
        numeros[id] = num;
    }
    int cuenta_par = 0;
    for(int indice = 0; indice < sizeof(numeros); indice++)
    {
        if (numeros[indice] % 2 == 0)
        {
            cuenta_par++;
        }
    }

    int cuenta_impar = 0;
    for (int idx = 0; idx < sizeof(numeros); idx++)
    {
        if (numeros[idx] % 2 != 0)
        {
            cuenta_impar++;
        }
    }
    cout <<"Tu lista es: " <<numeros << endl;
    cout <<"Tu lista tiene " <<cuenta_par <<" numeros pares" << endl;
    cout <<"Tu lista tiene " <<cuenta_impar <<" numeros impares" << endl;
}
