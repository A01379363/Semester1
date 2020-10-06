#include <iostream>

using namespace std;

int main(void)
{
    string nombre = "";
    int edad = 0;

    cout << "Hola C++!" << endl;
    cout << "Dame tu nombre:" << endl;
    cin >> nombre;
    cout << "Dame tu edad: " <<endl;
    cin >> edad;

    cout << "Hola " << nombre << " tu edad en 20 anos sera " << edad+20 << endl;

    return 0;
}
