#include <iostream>
using namespace std;

int m, n;
int height[501][501];
int dp[501][501];

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};

int dfs(int y, int x) {
    if (dp[y][x] != -1)
        return dp[y][x];
    
    int now = 0;
    int yy, xx;
    for (int i = 0; i < 4; i++) {
        yy = y + dy[i];
        xx = x + dx[i];
        if (yy < 0 || m <= yy || xx < 0 || n <= xx)
            continue;
        if (height[yy][xx] < height[y][x]) {
            now += dfs(yy, xx);
        }
    }
    dp[y][x] = now;
    return now;
}

int main() {
    cin >> m >> n;
    
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            cin >> height[i][j];
    
    fill_n(&dp[0][0], 501 * 501, -1);
    dp[m-1][n-1] = 1;
    
    cout << dfs(0, 0);
}
