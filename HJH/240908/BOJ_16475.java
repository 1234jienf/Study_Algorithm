package 자율팀스터디.d240907;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_16475 {
	static int n, m, k, l, p;
	static int mod;
	static int s, e;
	static int INF = Integer.MAX_VALUE / 2;
	static List<Edge>[][] graphs;
	static Set<Integer> traps = new HashSet<>();
	static int[][] dists;
	static boolean[][] visited;

	public static void main(String[] args) throws Exception {
		init();
		System.out.println(sol());
	}

	private static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());

		mod = 2 * p;

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < k; i++) {
			traps.add(Integer.parseInt(st.nextToken()));
		}

		dists = new int[n+1][];
		for (int i = 1; i <= n; i++) {
			dists[i] = new int[mod];
			Arrays.fill(dists[i], INF);
		}

		visited = new boolean[n+1][mod];

		int a, b, c;
		graphs = new ArrayList[2][n + 1];
		for (int i = 0; i < 2; i++)
			for (int j = 1; j <= n; j++)
				graphs[i][j] = new ArrayList<>();

		for (int i = l; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			graphs[0][a].add(new Edge(b, c));
			graphs[1][a].add(new Edge(b, c));
		}
		for (int i = 0; i < l; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			graphs[0][a].add(new Edge(b, c));
			graphs[1][b].add(new Edge(a, c));
		}

		st = new StringTokenizer(br.readLine());
		s = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
	}

	private static int sol() {
		// {노드, 거리, 누른횟수}
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) ->
			Integer.compare(a[1], b[1]));

		pq.add(new int[] {s, 0, 0});
		dists[s][0] = 0;

		int[] now;
		while (!pq.isEmpty()) {
			now = pq.poll();
			if (visited[now[0]][now[2] % mod])
				continue;
			visited[now[0]][now[2] % mod] = true;

			List<Edge>[] graph = graphs[now[2] / p % 2];
			for (Edge next : graph[now[0]]) {
				int pushed = now[2] + (traps.contains(next.v)? 1 : 0);
				if (dists[next.v][pushed % mod] <= now[1] + next.e)
					continue;
				dists[next.v][pushed % mod] = now[1] + next.e;
				pq.add(new int[] {next.v, dists[next.v][pushed % mod], pushed});
			}
		}

		int ans = INF;
		for (int i = 0; i < mod; i++) {
			ans = Math.min(dists[e][i], ans);
		}
		return ans == INF? -1 : ans;
	}

	static class Edge{
		int v, e;

		public Edge(int v, int e) {
			this.v = v;
			this.e = e;
		}
	}
}