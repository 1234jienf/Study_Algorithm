import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4485_녹색옷입은애가젤다지 {
	static final int INF = Integer.MAX_VALUE;
	static int[][] dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	static int N;
	static int[][] map;
	static int[][] dist;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int tc = 1;
		while (true) {
			N = Integer.parseInt(br.readLine()); // 동굴의 크기
			if (N == 0)
				break;
			map = new int[N][N];
			dist = new int[N][N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					dist[i][j] = Integer.MAX_VALUE;
				}
			}

			dist[0][0] = map[0][0];
			BFS(0, 0);
			
			sb.append("Problem " + tc + ": " + dist[N - 1][N - 1] + "\n");
			tc++;
		} // while
		System.out.println(sb);
		br.close();
	}// main

	static void BFS(int r, int c) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { r, c });

		while (!q.isEmpty()) {
			int[] t = q.poll();
			int x = t[0];
			int y = t[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dir[i][0];
				int ny = y + dir[i][1];
				if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
					if (dist[nx][ny] > dist[x][y] + map[nx][ny]) {
						dist[nx][ny] = dist[x][y] + map[nx][ny];
						q.add(new int[] { nx, ny });
					}
				}
			}
		}
	}
} 