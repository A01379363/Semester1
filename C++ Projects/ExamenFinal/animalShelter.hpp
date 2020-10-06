#include <iostream>
#include "animal.hpp"

using namespace std;

class AnimalShelter
{
    // Agregar los atributos faltantes
    private:
        int slotsAvailable, slotsUsed;
        Animal animalsInShelter[50];

    public:

        // Agregar los métodos faltantes
        AnimalShelter()
        {
            slotsAvailable = 50;
            slotsUsed = 0;
        }

        addAnimal(Animal animal_)
        {
            if (slotsUsed < slotsAvailable){
                animalsInShelter[slotsUsed] = animal_;
                slotsUsed++;
            } else {
                cout << "There is no more space for another animal" << endl;
            }
        }

        printAnimalById(int id_)
        {
            for (int i = 0; i < 50; i++){
                if (animalsInShelter[i].getId() == id_){
                    animalsInShelter[i].printInfo();
                }
            }
        }

        printAnimalsByAge(int age_)
        {
            for (int i = 0; i < 50; i++){
                if (animalsInShelter[i].getAge() == age_){
                    animalsInShelter[i].printInfo();
                }
            }
        }

        printAnimalsByAvailability(bool availability_)
        {
            for (int i = 0; i < 50; i++){
                if (animalsInShelter[i].availability == availability_){
                    animalsInShelter[i].printInfo();
                }
            }
        }

        printAnimalsByType(string type_)
        {
            for (int i = 0; i < 50; i++){
                if (animalsInShelter[i].getType() == type_){
                    animalsInShelter[i].printInfo();
                }
            }
        }
};
