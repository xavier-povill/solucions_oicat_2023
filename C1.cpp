#include <iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >> b) {
        if(a > 21 or b > 21) {
            // Cas on el guanyador ha fet mes de 21 punts. 
            // Sera valid si la diferencia es de 2 punts.
            if(abs(a-b) == 2) {
                cout << "SI" << endl;
            } 
            else {
                cout << "NO" << endl;
            }
        }
        else if(a == 21) {
            // Cas on A guanya amb 21 punts.
            // Sera valid si B fa menys de 20 punts.
            if(b < 20) {
                cout << "SI" << endl;
            }
            else {
                cout << "NO" << endl;
            }
        }
        else if(b == 21) {
            // Cas on B guanya amb 21 punts.
            // Sera valid si A fa menys de 20 punts.
            if(a < 20) {
                cout << "SI" << endl;
            }
            else {
                cout << "NO" << endl;
            }
        }
        else {
            // Cap dels 2 jugadors arriba a 21 punts.
            // Mai pot ser una puntuacio valida.
            cout << "NO" << endl;
        } 
    }
}