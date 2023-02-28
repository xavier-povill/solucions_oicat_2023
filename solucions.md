# Solucions Classificatori OICat 2023

:warning: __AQUEST DOCUMENT ENCARA NO ESTÀ ACABAT I POT CONTENIR ERRORS__

## Taula de continguts
* [Problema C1. Ping-pong](#C1)
* [Problema C2. L'ase d'en Buridan](#C2)
* [Problema Q1. Productes acabats en cinc](#Q1)
* [Problema C3. Redistribució de la riquesa](#C3)
* [Problema G1. Trencaclosques](#G1)
* [Problema C4. Camp de visió](#C4)
* [Problema Q2. Classificació de l'OICat](#Q2)
* [Problema G2. Ordenant llibres](#G2)
* [Problema C5. Distàncies a les fulles](#C5)
* [Problema G3. Pizzeries](#G3)
* [Problema C6. Comptant permutacions](#C6)
* [Problema C7. Retransmissió](#C7)


## [Problema C1. Ping-pong](https://jutge.org/problems/P90280_ca) <a name="C1"/>

Podem dividir el problema en 3 casos:
- Si el guanyador té més de 21 punts, la puntuació serà vàlida sempre i quan la diferència sigui de 2 punts.
- Si el guanyador té 21 punts, la puntuació serà vàlida si el perdedor té 19 o menys punts.
- Si el guanyador té menys de 21 punts, la puntuació mai pot ser vàlida.

<details>
  <summary><b>Codi (C++)</b></summary>

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

## [Problema C2. L'ase d'en Buridan](https://jutge.org/problems/P86377_ca) <a name="C2"/>

Ens podem guardar les mides dels sacs en un vector (o una llista en Python) i ordenar-les. Llavors, iterem de gran a petita fins que trobem un element repetit (o fins al final del vector, si no hi ha cap repetit), guardant-nos la suma dels sacs que portem menjats.

<details>
  <summary><b>Codi (C++)</b></summary>

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    while(cin >> n) {
        vector<int> v(n); // Declarem un vector de mida n.
        for(int i = 0; i < n; ++i) {
            cin >> v[i]; // Llegim els elements del vector.
        }
        sort(v.begin(), v.end()); // Ordenem el vector de petit a gran.
        int menjat = 0; // En aquesta variable anem sumant la mida dels sacs que ens mengem.
        for(int i = n-1; i >= 0; --i) {
            // Iterem pels elements del vector de gran a petit.
            if(i > 0 and v[i] == v[i-1]) {
                // La condicio i > 0 es necessaria perque, si no, quan i == 0,
                // al fer v[i-1] estariem accedint a la posicio -1 del vector
                // (que no existeix) i el programa podria fallar. 

                break; // Hem trobat un element repetit, per tant parem.
            }
            menjat += v[i]; // Sumem la mida del sac que ens mengem.
        }
        cout << menjat << endl;
    }
}
```
</details>

## [Problema Q1. Productes acabats en cinc](https://jutge.org/problems/P14803_ca) <a name="Q1"/>

La clau d'aquest problema era veure que, per tal que un nombre acabi en 5, ha de ser múltiple de 5 però no de 2.

Per tant, hem de comptar el nombre de subconjunts de { $1, 2, \dots, 50$ } que tenen algun múltiple de 5 però no tenen cap múltiple de 2 (és a dir, on tots els nombres son senars). Entre 1 i 50 hi ha 25 nombres senars, així que el nombre de subconjunts de nombres senars serà $2^{25}$ (per cada nombre senar tenim dues opcions: incloure'l o no incloure'l). Si a aquests els hi restem els $2^{20}$ que no tenen cap múltiple de 5, obtenim $2^{25} - 2^{20} = 32505856$. 

Una altra manera de pensar-ho és que per construir el subconjunt que volem hem de triar uns quants múltiples de 5 senars (tenim $2^5 - 1$ maneres de fer-ho, ja que per cada un dels 5 candidats el podem incloure o no incloure (això ens dona el terme $2^5$), però hem de restar 1 per no comptar el conjunt buit) i un conjunt de nombres senars no múltiples de 5 (d'aquests n'hi ha $2^{20}$ maneres, ja que no ens importa si està buit). Per tant, la resposta és $(2^{5} - 1) \cdot 2^{20}$, que dona el mateix que abans.

## [Problema C3. Redistribució de la riquesa](https://jutge.org/problems/P57539_ca) <a name="C3"/>

Expl

<details>
  <summary><b>Codi (C++)</b></summary>

```cpp
#include<bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    int n;
    ll k;
    while(cin >> n >> k) {
        vector<int> a(n);
        for(int& x : a)
            cin >> x;
        sort(a.begin(), a.end());

        // cost_esquerra[i] := diners que hem d'afegir per fer que els elements 
        //                     a l'esquerra d'a[i] siguin iguals a a[i].
        vector<ll> cost_esquerra(n, 0);
        for(int i = 1; i < n; ++i) {
            cost_esquerra[i] = cost_esquerra[i-1] + ll(a[i] - a[i-1]) * i;
        }

        // cost_dreta[i] := diners que hem de treure per fer que els elements 
        //                  a la dreta d'a[i] siguin iguals a a[i].
        vector<ll> cost_dreta(n, 0);
        for(int i = n-2; i >= 0; --i) {
            cost_dreta[i] = cost_dreta[i+1] + ll(a[i+1] - a[i]) * (n-1 - i);
        }

        int petit = -1; // maxim minim del vector que podem aconseguir afegint k euros.
        for(int i = 1; i < n; ++i) {
            if(cost_esquerra[i] > k) {
                ll sobrants = k - cost_esquerra[i-1];
                petit = a[i-1] + sobrants/i;
                break;
            }
        }
        if(petit == -1) {
            petit = a[n-1];
        }

        int gran = -1; // minim maxim del vector que podem aconseguir traient k euros.
        for(int i = n-2; i >= 0; --i) {
            if(cost_dreta[i] > k) {
                ll sobrants = k - cost_dreta[i+1];
                gran = a[i+1] - sobrants/(n-1 - i);
                break;
            }
        }
        if(gran == -1) {
            gran = a[0];
        }

        if(petit >= gran) {
            // Tot i que puguem moure molts diners, si la suma no 
            // es divisible per n no ho podrem igualar del tot.
            ll suma = 0;
            for(int& x : a) {
                suma += x;
            }
            cout << (suma%n ? 1 : 0) << endl;
        }
        else {
            cout << gran - petit << endl;
        }
    }
}
```
</details>

<details>
    <summary><b>Codi (Python3)</b></summary>

```py
from easyinput import read

n, k = read(int, int)
while n is not None:
    a = read(int, amount=n)
    if n == 1:
        a = [a] # si nomes hi ha un element, read(int) 
                # el llegeix com a enter, no com a llista
    a.sort()
    
    # cost_esquerra[i] := diners que hem d'afegir per fer que els elements 
    #                     a l'esquerra d'a[i] siguin iguals a a[i].
    cost_esquerra = [0] * n
    for i in range(1, n):
        cost_esquerra[i] = cost_esquerra[i-1] + (a[i] - a[i-1]) * i

    # cost_dreta[i] := diners que hem de treure per fer que els elements 
    #                  a la dreta d'a[i] siguin iguals a a[i].
    cost_dreta = [0] * n
    for i in range(n-2, -1, -1):
        cost_dreta[i] = cost_dreta[i+1] + (a[i+1] - a[i]) * (n-1 - i)

    petit = a[n-1] # maxim minim del vector que podem aconseguir afegint k euros.
    for i in range(1, n):
        if cost_esquerra[i] > k:
            sobrants = k - cost_esquerra[i-1]
            petit = a[i-1] + sobrants//i
            break

    gran = a[0] # minim maxim del vector que podem aconseguir traient k euros.
    for i in range(n-2, -1, -1):
        if cost_dreta[i] > k:
            sobrants = k - cost_dreta[i+1]
            gran = a[i+1] - sobrants//(n-1 - i)
            break

    if petit >= gran:
        # Tot i que puguem moure molts diners, si la suma no 
        # es divisible per n no ho podrem igualar del tot.
        if sum(a) % n == 0:
            print(0)
        else:
            print(1)
    else:
        print(gran - petit)

    n, k = read(int, int)
```
</details>