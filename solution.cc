#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<bool> vist;
vector<vector<int>> G;

void dfs(int u, int forbidden) {
	vist[u] = true;
	for(int v : G[u]) {
		if(v != forbidden and not vist[v]) {
			dfs(v, forbidden);
		}
	}
}

int main() {
	int n, m;
	while(cin >> n >> m) {
		G = vector<vector<int>>(n);
		for(int i = 0; i < m; ++i) {
			int u, v;
			cin >> u >> v;
			G[u].push_back(v);
			G[v].push_back(u);
		}

		int x, y;
		cin >> x >> y;
		if(x == y) cout << n-1 << endl;
		else {
			// Calculem punts d'articulacio que desconnecten x i y:
			vector<bool> artic(n, false);
			for(int v = 0; v < n; ++v) {
				vist = vector<bool>(n, false);
				dfs(x, v);
				if(not vist[y]) artic[v] = true;
			}


			int const INF = 1e9;
			vector<int> dist(n, INF);
			dist[x] = 0;
			priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
			pq.push({0, x});
			while(not pq.empty()) {
				pair<int,int> z = pq.top();
				pq.pop();
				int v = z.second;
				if(v == y) break;
				if(dist[v] != z.first) continue;
				for(int u : G[v]) {
					int d_arc = artic[u];
					if(dist[u] > dist[v] + d_arc) {
						dist[u] = dist[v] + d_arc;
						pq.push({dist[u], u});
					}
				}
			}
			if(artic[y]) dist[y]--;
			cout << n + dist[y] << endl;
		}
	}
}
