#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

class Vuelo{
public:
    int mes, terminal;
    string destino;
    string destinos[10] = {"MEX", "JFK" , "LAX", "GRU", "LCY", "CDG", "TXL", "PEK", "HKG", "SCL"};

    Vuelo(){
        terminal = 0;
        mes = 0;
        destino = "";
    }

    Vuelo(int _terminal, int _mes, int _destino){
        terminal = _terminal;
        mes = _mes;
        destino = destinos[_destino];
    }

};
