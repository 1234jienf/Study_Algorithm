import java.awt.*;
import java.io.*;
import java.util.*;

public class BOJ_21610_마법사상어와비바라기 {
	static int N, M;
	static int[][] map;
	static Queue<Point> clouds = new LinkedList<>();
	static int[] dx = { 0, 0, -1, -1, -1, 0, 1, 1, 1 };
	static int[] dy = { 0, -1, -1, 0, 1, 1, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		int answer = 0;

		map = new int[N + 1][N + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 초기 구름 생성
		clouds.add(new Point(N, 1));
		clouds.add(new Point(N, 2));
		clouds.add(new Point(N - 1, 1));
		clouds.add(new Point(N - 1, 2));

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int d = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());

			simulation(d, s);

		}

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				answer += map[i][j];
			}
		}
		System.out.println(answer);
	}

	static void simulation(int d, int s) {
		boolean[][] visit = new boolean[N + 1][N + 1];

		for (Point c : clouds) {
			// 1. 구름 이동
			c.x = (c.x + dx[d] * (s % N) + N) % N;
			c.y = (c.y + dy[d] * (s % N) + N) % N;

			if (c.x == 0)
				c.x = N;
			if (c.y == 0)
				c.y = N;
			// 2. 비 내림
			map[c.x][c.y]++;
		}

		while (!clouds.isEmpty()) {
			// 3. 구름 제거
			Point cur = clouds.poll();
			int cnt = 0;
			visit[cur.x][cur.y] = true;
			// 4. 대각선에 물이 있는 칸수 만큼 물 양 증가
			for (int i = 2; i <= 8; i += 2) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				// 경계 넘어간 칸은 세지 않는다
				if (nx < 1 || nx > N || ny < 1 || ny > N || map[nx][ny] <= 0)
					continue;
				cnt++;
			}
			map[cur.x][cur.y] += cnt;
		}

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (!visit[i][j] && map[i][j] >= 2) {
					map[i][j] -= 2;
					clouds.add(new Point(i, j));
				}
			}
		}

	}
}
