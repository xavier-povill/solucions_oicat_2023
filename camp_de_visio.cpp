#include<bits/stdc++.h>
using namespace std;

// Angle del punt (x, y) amb l'eix X. Retorna un valor en l'interval [-180, 180]:
// (per ex. angle(1, 0) = 0, angle(0, 1) = 90, angle(0, -1) = -90).
double angle(int x, int y) {
	return atan2(y, x) * 180 / M_PI;
}

int main() {
	int n, theta;
	while(cin >> n >> theta) {
		vector<double> a(n); // vector on guardem els angles dels punts.
		for(auto& d : a) {
			int x, y;
			cin >> x >> y;
			d = angle(x, y);
		}
		if(n == 1) {
			cout << 1 << endl;
			continue;
		}
		sort(a.begin(), a.end());
		int ans = 1; // màxim nombre de punts que podem veure.
		int r = 1;
		for(int l = 0; l < n; ++l) {
			// l := primer punt que veiem en sentit antihorari.
			// r := primer punt que no veiem en sentit antihorari des de l.

			// Augmentem r fins que no poguem veure el punt r.
			while(a[r%n] - a[l] + (r%n < l? 360 : 0) <= theta) {
				++r;
				if(r%n == l) break;
			}
			ans = max(ans, r - l); // començant des de l podem veure un total de r-l punts.
		}
		cout << ans << endl;
	}
}