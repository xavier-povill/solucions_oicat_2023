#include<bits/stdc++.h>
using namespace std;

int main(){
	// PRECONDICIÓ: G es un arbre
	// Complexitat: O(n+m)
	int n, m;
	while(cin >> n >> m) {
		vector<vector<int>> G(n);
		for(int i = 0; i < m; ++i) {
			int a, b;
			cin >> a >> b;
			G[a].push_back(b);
			G[b].push_back(a);
		}
		int x, y;
		cin >> x >> y;

		// BFS des de x:
		vector<int> dist(n, -1);
		dist[x] = 0;
		queue<int> q;
		q.push(x);
		while(not q.empty()) {
		    int v = q.front();
		    q.pop();
		    for(int u : G[v]) {
		    	if(dist[u] == -1) {
		    		dist[u] = dist[v] + 1;
		    		// Podem acabar el BFS si ja hem arribat a y, ja que 
		    		// la seva distància no canviarà més.
		    		if(u == y) 
		    		    break;
		    		q.push(u);
		    	}
		    }
		}
		cout << n-1 + dist[y] << endl;
	}
}