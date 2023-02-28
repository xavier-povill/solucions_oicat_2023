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
		//                     a la dreta d'a[i] siguin iguals a a[i].
		vector<ll> cost_dreta(n, 0);
		for(int i = n-2; i >= 0; --i) {
			cost_dreta[i] = cost_dreta[i+1] + ll(a[i+1] - a[i]) * (n-i-1);
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
				gran = a[i+1] - sobrants/(n-i-1);
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