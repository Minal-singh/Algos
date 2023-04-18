int dijkstra(int n, vector<pair<int,int>> &graph, int node1, int node2){
    vector<int> dist(n+1, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[node1] = 0;
    pq.push({0, node1});
    while(!pq.empty()){
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        if(u == node2) return d;
        if(d > dist[u]) continue;
        for(auto &v: graph[u]){
            if(dist[u] + v.second < dist[v.first]){
                dist[v.first] = dist[u] + v.second;
                pq.push({dist[v.first], v.first});
            }
        }
    }
    return -1;
}
