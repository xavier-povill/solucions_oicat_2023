<<<<<<< HEAD
 Solucions Classificatori OICat 2023
=======
 Solucions Final OICat 2022
>>>>>>> 34feafac108cf7d95dd71dfb78de27196231e0ea

:warning: __AQUEST DOCUMENT ENCARA NO ESTÀ ACABAT I POT CONTENIR ERRORS__

## Taula de continguts
* [Problema C1. Ping-pong](#C1)


## [Problema C1. Ping-pong](https://jutge.org/problems/) <a name="C1"/>

Explicació

<details>
  <summary><b>Codi</b></summary>

```cpp
#include <iostream>
using namespace std;
int main() {
    int a, b;
    while(cin >> a >> b) {
        if(a > 21 or b > 21) {
            if(abs(a-b) == 2) {
                cout << "SI" << endl;
            } 
            else {
                cout << "NO" << endl;
            }
        }
        else if(a == 21) {
            if(b <= 19) {
                cout << "SI" << endl;
            }
            else {
                cout << "NO" << endl;
            }
        }
        else if(b == 21) {
            if(a <= 19) {
                cout << "SI" << endl;
            }
            else {
                cout << "NO" << endl;
            }
        }
        else {
            cout << "NO" << endl;
        } 
    }
}
```
</details>
<details>
<<<<<<< HEAD
  <summary><b>El mateix codi però una mica més elegant</b></summary>
=======
  <summary><b>Codi una mica més elegant</b></summary>
>>>>>>> 34feafac108cf7d95dd71dfb78de27196231e0ea

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