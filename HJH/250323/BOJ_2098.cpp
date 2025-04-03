#define _GLIBCXX_HOSTED 1
#include <bits/stdc++.h>
#define MAX_N   16
#define MAX_V   65536
#define INF     1E8
using namespace std;

int n;
int w[MAX_N][MAX_N];
int dp[MAX_N][MAX_V];
int done;

void input() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> w[i][j];
        }
    }
}

int tsp(int now, int visited) {
    if (visited == done) {
        return w[now][0] ? w[now][0] : INF;
    }
    if (dp[now][visited] != -1) {
        return dp[now][visited];
    }
    
    dp[now][visited] = INF;
    for (int i = 1; i < n; i++) {
        if ((visited & (1 << i)) == 0 && w[now][i]) {
            int cost = tsp(i, visited | (1 << i)) + w[now][i];
            if (cost < dp[now][visited])
                dp[now][visited] = cost;
        }
    }
    return dp[now][visited];
}

void show () {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < done; j++){
            cout << "\t" << dp[i][j];
        }
        cout << endl;
    }
}

void sol() {
    done = (1 << n) - 1;
    fill(&dp[0][0], &dp[MAX_N-1][MAX_V], -1);
    cout << tsp(0, 1);
    show();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    input();
    sol();
}
