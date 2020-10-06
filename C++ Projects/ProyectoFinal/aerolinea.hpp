#include <string>
#include <cstdlib>
#include <ctime>
#include "vuelo.hpp"

using namespace std;

class Aerolinea{
public:
    string nombre;
    string nombres[10] = {"AeroMexico", "American Airlines" , "Delta", "LATAM", "British Airways", "Air France", "Lufthansa", "United", "Copa Airlines", "Aeromar"};

    Vuelo vuelos[10];

    Aerolinea(){
        nombre = nombres[rand() % 10];
    }

    Aerolinea(int _nombre){
        nombre = nombres[_nombre];
    }

};
