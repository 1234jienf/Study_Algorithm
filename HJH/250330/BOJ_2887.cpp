#define _GLIBCXX_HOSTED 1
#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef struct{
    int dist, a, b;
} edge;

int n, x, y, z;
vector<int*> stars;
vector<edge> edges;

int roots[100000] = {};

int find(int node) {
    if (roots[node] == node) return node;
    return roots[node] = find(roots[node]);
}

bool unite(int a, int b) {
    int ra = find(a);
    int rb = find(b);
    if (ra == rb) return false;
    roots[rb] = ra;
    return true;
}

int main(){
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x >> y >> z;
        stars.push_back(new int[] {x, y, z, i});
        roots[i] = i;
    }
    for (int x = 0; x < 3; x++) {
        sort(stars.begin(), stars.end(),
             [x](int *a, int *b) -> bool
             {return a[x] < b[x];});
        
        for (int i = 1; i < n; i++) {
            edges.push_back({stars[i][x] - stars[i-1][x], stars[i][3], stars[i-1][3]});
        }
    }
    
    sort(edges.begin(), edges.end(),
         [](edge a, edge b) -> bool
         {return a.dist < b.dist;});
    
    ll ans = 0L;
    for (edge e : edges) {
        if (unite(e.a, e.b)) {
            ans += e.dist;
        }
    }
    cout << ans;
}
