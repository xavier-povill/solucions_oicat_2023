#include<bits/stdc++.h>
using namespace std;

// retorna un valor en [-180, 180]
double angle(int x, int y) {
	return atan2(y, x) * 180 / M_PI;
}

int main() {
	int n, theta;
	while(cin >> n >> theta) {
		vector<double> a(n);
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
		int ans = 1;
		int r = 1; // r := primer objecte que no veiem en sentit antihorari
		for(int l = 0; l < n; ++l) {
			// l := primer objecte que veiem en sentit antihorari
			while(a[r%n] - a[l] + (r%n < l? 360 : 0) <= theta) {
				++r;
				if(r%n == l) break;
			}
			ans = max(ans, r - l);
		}
		cout << ans << endl;
	}
}