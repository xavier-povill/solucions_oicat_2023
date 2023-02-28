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
		int minim = a[0]; // min_i {a_i} que podem aconseguir afegint k euros
		ll y = 0; // nombre de euros que portem afegits
		int esq = 1; // invariant: podem fer que tots els elements de a[0..esq-1] 
		             // siguin majors o iguals a 'minim' afegint 'y' euros
		while(esq < n and y < k) {
			ll inc = min(ll(a[esq] - a[esq-1])*esq, k-y); 
			minim += inc/esq;
			y += inc;
			esq++;
		}
		int maxim = a[n-1]; // max_i {a_i} que podem aconseguir traient k euros
		y = 0; // nombre de euros que portem trets
		int dre = n-2; // invariant: podem fer que tots els elements de a[dre+1..n-1] 
		               // siguin menors o iguals a 'maxim' traient 'y' euros
		while(dre >= 0 and y < k) {
			ll inc = min(ll(a[dre+1] - a[dre])*(n-dre-1), k-y);
			maxim -= inc/(n-dre-1);
			y += inc;
			dre--;
		}

		if(minim >= maxim) {
			// tot i que puguem moure molts diners, si la suma no es divisible per n 
			// mai no podrem igualar-ho del tot
			ll suma = 0;
			for(int& x : a) 
				suma += x;
			cout << (suma%n ? 1 : 0) << endl;
		}
		else cout << maxim-minim << endl;
	}
}