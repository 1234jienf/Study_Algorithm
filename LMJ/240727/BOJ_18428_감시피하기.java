import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_18428_감시피하기 {
	static int N;
	static int[][] map;
	static List<Point> teachers = new ArrayList<>();
	static boolean possible = false;
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { -1, 0, 1, 0 };

	// 빈칸:0, 선생:1, 학생:2, 장애물:3
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		map = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				String s = st.nextToken();
				if (s.equals("T")) {
					teachers.add(new Point(i, j));
					map[i][j] = 1;
				} else if (s.equals("S")) {
					map[i][j] = 2;
				}
			}
		}

		dfs(0);

		if (possible) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}

	}

	static void dfs(int n) {
		if (n == 3) {
			if (!possible && check()) {
				possible = true;
			}
			return;
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (map[i][j] == 0) {
					map[i][j] = 3;
					dfs(n + 1);
					map[i][j] = 0;
				}
			}
		}
	}

	static boolean check() {
		for (Point t : teachers) {
			for (int k = 0; k < 4; k++) {
				int x = t.x;
				int y = t.y;
				while (true) {
					x += dx[k];
					y += dy[k];
					if(x<0 || x>=N || y<0 || y>=N || map[x][y]==3) break;
					if(map[x][y]==2) return false;
				}
			}
		}

		return true;
	}
}
