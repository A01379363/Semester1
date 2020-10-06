/*
+
+
+
NO MODIFICAR ESTE CODIGO
+
+
+
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

#include "animalShelter.hpp"

using namespace std;

int main(void)
{
    srand(time(0));
    
    string animalTypes[4] = {"Cat", "Dog", "Bird", ""};

    AnimalShelter shelter;

    for(int idx = 0; idx < 55; idx++)
    {
        bool availability = rand() % 50 < 25 ? true: false;
        Animal animal(idx, rand() % 33 - 16, availability, animalTypes[rand() % 4]);
        shelter.addAnimal(animal);
    }

    cout << endl <<"-- Searching for id 23: " << endl;

    shelter.printAnimalById(23);

    cout << endl <<"-- Searching for animals aged 5: " << endl;

    shelter.printAnimalsByAge(5);

    cout << endl <<"-- Searching for animals ready for adoption: " << endl;

    shelter.printAnimalsByAvailability(true);

    cout << endl <<"-- Searching for cats: " << endl;

    shelter.printAnimalsByType("Cat");
}
    
