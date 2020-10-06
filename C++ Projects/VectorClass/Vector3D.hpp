#include <cmath>

using namespace std;

class Vector3D
{
public:
    float x, y, z;
    float xOrigen, yOrigen, zOrigen;

    Vector3D(float x_, float y_, float z_,
              float xOrigen_ = 0,
              float yOrigen_ = 0,
              float zOrigen_ = 0)
    {
        x = x_;
        y = y_;
        z = z_;
        xOrigen = xOrigen_;
        yOrigen = yOrigen_;
        zOrigen = zOrigen_;

    }

    float magnitud(void)
    {
        return sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    }
    Vector3D unit(void)
    {
        float mag = magnitud();
        return Vector3D(x/mag, y/mag, z/mag);
    }

};
