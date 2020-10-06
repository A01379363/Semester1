#include <iostream>
#include <cstdlib>
#include <ctime>
#include "aeropuerto.hpp"

using namespace std;

int main(void)
{

    string nombres[10] = {"AeroMexico", "American Airlines" , "Delta", "LATAM", "British Airways", "Air France", "Lufthansa", "United", "Copa Airlines", "Aeromar"};
    string destinos[10] = {"MEX", "JFK" , "LAX", "GRU", "LCY", "CDG", "TXL", "PEK", "HKG", "SCL"};
    srand(time(0));

    Aeropuerto aeropuerto("AICM");
    int numVuelosDestino[10] = {0};
    int numVuelosMes[12] = {0};
    int numVuelosTerminal[2] = {0};
    int numVuelosAerolinea[10] = {0};


    for(int i = 0; i < 10; i++){ // crea 10 vuelos por cada aerolinea osea 100 vuelos en total
        for(int j = 0; j < 10; j++){
            Vuelo Vuelo((rand()%2)+1, (rand()%12)+1, (rand()%10)); // utiliza numeros random para generar la terminal, el mes y el destino
              aeropuerto.aerolineas[i].vuelos[j] = Vuelo;
        }
    }
    for (int i = 0; i < 10; i++){ // es un counter que cuenta el numero de vuelos en cada aerolinea
        for (int j = 0; j < 10; j++){
            if (aeropuerto.aerolineas[i].nombre == "AeroMexico"){
                numVuelosAerolinea[0]++;
            } else if (aeropuerto.aerolineas[i].nombre == "American Airlines"){
                numVuelosAerolinea[1]++;
            } else if (aeropuerto.aerolineas[i].nombre == "Delta"){
                numVuelosAerolinea[2]++;
            } else if (aeropuerto.aerolineas[i].nombre == "LATAM"){
                numVuelosAerolinea[3]++;
            } else if (aeropuerto.aerolineas[i].nombre == "British Airways"){
                numVuelosAerolinea[4]++;
            } else if (aeropuerto.aerolineas[i].nombre == "Air France"){
                numVuelosAerolinea[5]++;
            } else if (aeropuerto.aerolineas[i].nombre == "Lufthansa"){
                numVuelosAerolinea[6]++;
            } else if (aeropuerto.aerolineas[i].nombre == "United"){
                numVuelosAerolinea[7]++;
            } else if (aeropuerto.aerolineas[i].nombre == "Copa Airlines"){
                numVuelosAerolinea[8]++;
            } else if (aeropuerto.aerolineas[i].nombre == "Aeromar"){
                numVuelosAerolinea[9]++;
            }
        }
    }


    for(int i = 0; i < 10; i++){ // imprime el numero de vuelos para las aerolineas
        cout << "Numero de Vuelos en " << nombres[i] << ": " << numVuelosAerolinea[i]  << endl;
    }

    cout << "------------------------------------------------------" << endl;

    for (int i = 0; i < 10; i++){ // es un counter que cuenta el numero de vuelos en cada destino
        for(int j = 0; j < 10; j++){
            if (aeropuerto.aerolineas[i].vuelos[j].destino == "MEX"){
                numVuelosDestino[0]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "JFK"){
                numVuelosDestino[1]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "LAX"){
                numVuelosDestino[2]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "GRU"){
                numVuelosDestino[3]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "LCY"){
                numVuelosDestino[4]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "CDG"){
                numVuelosDestino[5]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "TXL"){
                numVuelosDestino[6]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "PEK"){
                numVuelosDestino[7]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "HKG"){
                numVuelosDestino[8]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].destino == "SCL"){
                numVuelosDestino[9]++;
            }
        }
    }

    for(int i = 0; i < 10; i++){ // imprime el numero de vuelos para cada destino
        cout << "Numero de Vuelos con destino a " << destinos[i] << ": " << numVuelosDestino[i]  << endl;
    }
    cout << "------------------------------------------------------" << endl;

    for (int i = 0; i < 10; i++){ // es un counter que cuenta el numero de vuelos en cada mes
        for(int j = 0; j < 10; j++){
            if (aeropuerto.aerolineas[i].vuelos[j].mes == 1){
                numVuelosMes[0]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 2){
                numVuelosMes[1]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 3){
                numVuelosMes[2]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 4){
                numVuelosMes[3]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 5){
                numVuelosMes[4]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 6){
                numVuelosMes[5]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 7){
                numVuelosMes[6]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 8){
                numVuelosMes[7]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 9){
                numVuelosMes[8]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 10){
                numVuelosMes[9]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 11){
                numVuelosMes[10]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].mes == 12){
                numVuelosMes[11]++;
            }
        }
    }
    for(int i = 0; i < 12; i++){ // imprime el numero de vuelos para cada mes
        cout << "Numero de Vuelos en el mes " << i+1 << ": " << numVuelosMes[i]  << endl;
    }
    cout << "------------------------------------------------------" << endl;

    for (int i = 0; i<10; i++){ // es un counter que cuenta el numero de vuelos en cada terminal
        for(int j = 0; j < 10; j++){
            if (aeropuerto.aerolineas[i].vuelos[j].terminal == 1){
                numVuelosTerminal[0]++;
            } else if (aeropuerto.aerolineas[i].vuelos[j].terminal == 2){
                numVuelosTerminal[1]++;
            }
        }
    }

    if (numVuelosTerminal[0] > numVuelosTerminal[1]){ // decide que mensaje imprimir dependiendo de que terminal tiene mas vuelos
        cout << "La terminal 1 tuvo mas vuelos" << endl;
    } else if (numVuelosTerminal[0] < numVuelosTerminal[1]){
        cout << "La terminal 2 tuvo mas vuelos" << endl;
    } else {
        cout << "Las dos terminales tuvieron la misma cantidad de vuelos" << endl;
    }
}

