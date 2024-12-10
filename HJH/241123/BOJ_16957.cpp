#include <iostream>
#include <vector>
#define loop(i, a, b) for(int i = a; i < b; i++)
#define endl "\n"

using namespace std;

int board[500][500];
pair<int, int> roots[500][500];

int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};

pair<int, int> find(int x, int y) {
    if (roots[x][y].first == x && roots[x][y].second == y)
        return roots[x][y];
    roots[x][y] = find(roots[x][y].first, roots[x][y].second);
    return roots[x][y];
}

// 뒤 좌표를 앞 좌표에 종속시키기.
void ds(int x, int y, int xx, int yy) {
    pair<int, int> r = find(x, y);
    pair<int, int> rr = find(xx, yy);
    roots[rr.first][rr.second] = r;
}

vector<vector<int>> sol(int r, int c) {
    loop(i, 0, r)
        loop(j, 0, c)
            roots[i][j] = {i, j};
    
    // 주변에서 제일 작은 칸을 찾아 종속시킨다.
    int ii, jj, val;
    loop(i, 0, r) {
        loop(j, 0, c) {
            ii = -1;
            jj = -1;
            val = board[i][j];
            loop(d, 0, 8) {
                int ti = i + dx[d];
                int tj = j + dy[d];
                if (ti < 0 || ti >= r || tj < 0 || tj >= c) continue;
                if (val > board[ti][tj]) {
                    val = board[ti][tj];
                    ii = ti;
                    jj = tj;
                }
            }
            if (ii != -1)
                ds(ii, jj, i, j);
        }
    }
    vector<vector<int>> ans (r, vector<int>(c));
    loop(i, 0, r) {
        loop(j, 0, c) {
            pair<int, int> tmp = find(i, j);
            ++ans[tmp.first][tmp.second];
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int r, c;
    cin >> r >> c;
    
    loop(i, 0, r) {
        loop(j, 0, c) {
            cin >> board[i][j];
        }
    }
    // 유니온파인드를 적용하자
    vector<vector<int>> result = sol(r, c);
    
    loop(i, 0, r) {
        loop(j, 0, c) {
            cout << result[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}