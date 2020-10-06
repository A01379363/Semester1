#include <string>
#include <cstdlib>
#include <ctime>
#include "aerolinea.hpp"

using namespace std;

class Aeropuerto{
public:
    string nombre;


    Aerolinea aerolineas[10];

    Aeropuerto(){
        nombre = "Aeropuerto Internacional de la Ciudad de Mexico";

    }

    Aeropuerto(string _nombre){
        nombre = _nombre;
        for(int i=0; i < 10; i++)
            aerolineas[i] = Aerolinea(i);
    }


};
