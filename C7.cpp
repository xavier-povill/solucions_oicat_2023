#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<bool> vist;
vector<vector<int>> G;

// Fa un dfs des de u, sense visitar mai el vèrtex prohibit.
void dfs(int u, int prohibit) {
	vist[u] = true;
	for(int v : G[u]) {
		if(v != prohibit and not vist[v]) {
			dfs(v, prohibit);
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
			// artic[v] = true si v és un punt d'articulació que 
			// desconnecta x i y al treure'l del graf.
			vector<bool> artic(n, false); 
			for(int v = 0; v < n; ++v) {
				vist = vector<bool>(n, false);
				// Fem un DFS des de x on el vertex v està "prohibit" i no hi podem passar.
				dfs(x, v); 
				if(not vist[y]) artic[v] = true;
			}

			// Fem un Dijkstra des de x fins a y on els arcs que duen a punts d'articulació 
			// que desconnecten x i y tenen cost 1. Així, dist[y] serà el mínim nombre de 
			// punts d'articulació pels quals hem de passar en un camí de x a y.
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
			// Si y mateix és un punt d'articulació l'haurem comptat en la distància 
			// (i no l'hem de comptar).
			if(artic[y]) dist[y]--; 
			cout << n + dist[y] << endl;
		}
	}
}
