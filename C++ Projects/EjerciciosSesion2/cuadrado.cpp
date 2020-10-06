#include <iostream>

using namespace std;

void cuadrado(int width, int height)
{
    if (width % 2 == 0)
    {
        width++;
    }
    if (height % 2 == 0)
    {
        height++;
    }
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            if ((0 < row && row < height-1) && (0 < col && col < width-1))
            {
                cout <<" ";
            }
            else if (col % 2 == 0)
            {
                cout <<"+";
            }
            else
            {
                cout <<"-";
            }

        }
        cout <<"" << endl;
    }
}

int main(void)
{
    int alto = 0;
    int ancho = 0;
    cout <<"Dame el alto del cuadrado: " << endl;
    cin >> alto;
    cout <<"Dame el ancho del cuadrado: " << endl;
    cin >> ancho;
    cuadrado(ancho, alto);
}
