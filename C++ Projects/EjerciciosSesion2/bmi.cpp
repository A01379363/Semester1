#include <math.h>
#include <iostream>

using namespace std;

void bmi(float height, float weight)
{
    float indice = 0;
    indice = weight / pow(height, 2);

    if(indice<20)
    {
        cout << "Peso bajo" <<endl;
    }
    else if(indice<25)
    {
        cout << "Normal" <<endl;
    }
    else if(indice<30)
    {
        cout << "Sobre peso" <<endl;
    }
    else if(indice<40)
    {
        cout << "Obesidad" <<endl;
    }
    else
    {
        cout << "Obesidad morbida" <<endl;
    }

}

int main(void)
{
    float height = 0;
    float weight = 0;
    cout << "Dame tu altura: " <<endl;
    cin >> height;
    cout << "Dame tu peso: " <<endl;
    cin >> weight;

    bmi(height, weight);
}
