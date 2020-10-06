#include <iostream>

using namespace std;

class Animal
{
    // Agregar los atributos faltantes
    private:
        int age, id;
        string type;

    public:

        bool availability;
        // Agregar los métodos y constructores faltantes
        Animal()
        {
            id = 0;
            age = 0;
            availability = false;
            type = "";
        }
        Animal(int id_, int age_, bool availability_, string type_)
        {
            if (id_ > 0){
                id = id_;
            } else {
                id = 0;
            }
            if (age_ >= 0){
                age = age_;
            } else {
                age = 1;
            }

            availability = availability_;

            if (type_ == "Cat" || type_ == "Dog" || type_ == "Bird"){
                type = type_;
            } else {
                type = "Undefined";
            }
        }

        int getAge() { return age; }
        int getId() { return id; }
        string getType() { return type; }

        setAge(int age_)
        {
            if (age_ >= 0){
                age = age_;
            } else {
                age = 1;
            }
        }

        setID(int id_)
        {
            if (id_ > 0){
                id = id_;
            } else {
                id = 0;
            }
        }

        setType(string type_)
        {
            if (type_ == "Cat" || type_ == "Dog" || type_ == "Bird"){
                type = type_;
            } else {
                type = "Undefined";
            }
        }
        void printInfo()
        {
            cout << "ID: " << id << endl;
            cout << "Age: " << age << endl;
            cout << "Type: " << type << endl;
            cout << "Available for adoption: " << availability << endl;
            cout << endl;
        }
};
