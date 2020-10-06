#include <iostream>
#include "Vector3D.hpp"

using namespace std;

int main(void)
{
    Vector3D vector1(5, 6, 2);
    Vector3D vector2(1, 2, 3);

    cout << vector1.x << "," << vector1.y << "," << vector1.z << endl;
    cout << vector2.x << "," << vector2.y << "," << vector2.z << endl;

    cout << "La magnitud del Vector 1 es: " << vector1.magnitud() << endl;
    Vector3D unitarioVector1 = vector1.unit();
    cout << unitarioVector1.x << "," << unitarioVector1.y << "," << unitarioVector1.z << endl;

    cout << "La magnitud del Vector 2 es: " << vector2.magnitud() << endl;
    Vector3D unitarioVector2 = vector2.unit();
    cout << unitarioVector2.x << "," << unitarioVector2.y << "," << unitarioVector2.z << endl;

    return 0;

}
