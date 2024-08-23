import java.io.*;
import java.util.*;

public class BOJ_3678_카탄의개척자 {
	static int N;
	static int map[][] = new int[2001][2001];
	static final int stand = 1000;
	static int res[] = new int[6];
    static int ans[] = new int[10001];
    static boolean[] check = new boolean[6];
    static int dx[] = { -1, 1, 2, 1, -1, -2 };
	static int dy[] = { -1, -1, 0, 1, 1, 0 };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        res[1] = 1;
        res[2] = 1;
        int x = stand;
        int y = stand;
        int d = 5;
        map[x][y] = 1;
        x-=1;
        y+=1;
        map[x][y] = 2;
        ans[1] = 1;
        ans[2] = 2;

        for(int i = 2; i<10000;i++){
            int nd = (d+1)%6;
            int nx = x + dx[nd];
            int ny = y + dy[nd];
            if(map[nx][ny]!=0){
                nx = x + dx[d];
                ny = y + dy[d];
                nd = d;
            }

            x = nx;
            y = ny;
            d = nd;

            Arrays.fill(check, false);
            for(int dir = 0; dir<6;dir++){
                nx = x + dx[dir];
                ny = y + dy[dir];
                check[map[nx][ny]] = true;
            }
            int c = 1;
            for(c=1;c<=5;c++){
                if(!check[c]) break;
            }

            int minValue = res[c];

            for(int r = c+1; r<=5;r++){
                if (minValue > res[r]&&!check[r]) {
					minValue = res[r];
					c = r;
				}
			}

            map[x][y] = c;
			ans[i + 1] = c;
			res[c]++;

        }
        
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t<T;t++){
            int tc = Integer.parseInt(br.readLine());
            bw.append(ans[tc]+"\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}