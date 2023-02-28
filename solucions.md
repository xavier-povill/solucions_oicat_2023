# Solucions Classificatori OICat 2023

:warning: __AQUEST DOCUMENT ENCARA NO ESTÀ ACABAT I POT CONTENIR ERRORS__

## Taula de continguts
* [Problema C1. Ping-pong](#C1)


## [Problema C1. Ping-pong](https://jutge.org/problems/) <a name="C1"/>

Podem dividir el problema en 3 casos:
- Si el guanyador té més de 21 punts, la puntuació serà vàlida sempre i quan la diferència sigui de 2 punts.
- Si el guanyador té 21 punts, la puntuació serà vàlida si el perdedor té 19 o menys punts.
- Si el guanyador té menys de 21 punts, la puntuació mai pot ser vàlida.

<details>
  <summary><b>Codi</b></summary>

```cpp
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
```
</details>
<details>
  <summary><b>El mateix codi però una mica més elegant</b></summary>

```cpp
#include <iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >> b) {
        if(a < b) swap(a, b);
        if(a > 21) cout << (a-b == 2? "SI" : "NO") << endl;
        else if(a == 21) cout << (b <= 19? "SI" : "NO") << endl;
        else cout << "NO" << endl;
    }
}
```
</details>

## [Problema C2. Ase de Buridan](https://jutge.org/problems/) <a name="C2"/>

Explicació

<details>
  <summary><b>Codi</b></summary>

```cpp
#include <iostream>
using namespace std;
int main() {
    
}
```
</details>